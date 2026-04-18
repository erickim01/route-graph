import requests
import json
from pathlib import Path
from typing import Any

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"

class WarApiClient:
    """Foxhole War API wrapper with built-in caching for active regions."""

    def __init__(self, cache_dir: Path | None = None) -> None:
        """Initialize client with optional cache directory."""
        self.cache_dir = cache_dir or Path.home() / ".foxhole_logi"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._active_regions_cache_file = self.cache_dir / "active_regions.json"
        self._war_number = None  # placeholder for future "new war" detection
        self.session = requests.Session()  # reuse TCP connections across calls

    def get_war_data(self) -> dict[str, Any]:
        """Fetch current war information."""
        return self._get_json("/war")

    def get_active_regions(self) -> list[str]:
        """Return list of active map/region names, using cache when possible."""
        if not self._active_regions_cache_file.exists():
            data = self._fetch_active_regions()
            self._save_to_cache(data)
            return data

        with open(self._active_regions_cache_file) as f:
            return json.load(f)

    def get_map_data(self) -> dict[str, Any]:
        """Fetch raw map list data (note: endpoint ends with slash in original)."""
        return self._get_json("/maps/")

    def _fetch_active_regions(self) -> list[str]:
        """Internal fetch for active regions (used by caching logic)."""
        return self._get_json("/maps")

    def _save_to_cache(self, regions: list[str]) -> None:
        """Save active regions list to JSON cache file."""
        with open(self._active_regions_cache_file, "w") as f:
            json.dump(regions, f)

    def _get_json(self, endpoint: str) -> Any:
        """Private helper: performs GET and returns parsed JSON."""
        r = self.session.get(f"{BASE_URL}{endpoint}")
        r.raise_for_status()
        return r.json()         




import requests
import json
from pathlib import Path

BASE_URL = "https://war-service-live.foxholeservices.com/api"

class WarApiClient:
    def __init__(self, cache_dir: Path | None = None):
        self.cache_dir = cache_dir or Path.home() / ".foxhole_logi"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._active_regions_cache_file = self.cache_dir / "active_regions.json"
        self._war_number = None  # we'll use this later for "new war" detection

    def get_active_regions(self) -> list[str]:
        # First run or cache missing → fetch and save
        if not self._active_regions_cache_file.exists():
            data = self._fetch_active_regions()
            self._save_to_cache(data)
            return data

        # Load from cache (we'll add new-war refresh later)
        with open(self._active_regions_cache_file) as f:
            return json.load(f)

    def _fetch_active_regions(self) -> list[str]:
        r = requests.get(f"{BASE_URL}/worldconquest/maps")
        r.raise_for_status()
        return r.json()  # returns list of active map names

    def _save_to_cache(self, regions: list[str]) -> None:
        with open(self._active_regions_cache_file, "w") as f:
            json.dump(regions, f)