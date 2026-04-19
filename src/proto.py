import requests
import requests_cache
from typing import Any
from pathlib import Path

### Wrapper to War API
#
# URL Construction
#
# Response Handling
#
# Static Caching

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"   #For now this goes to Able only


def get_war_data() -> dict[str, Any]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
    r = requests.get(f"{BASE_URL}/war")
    r.raise_for_status()
    return r.json()

#Returns Valid Regions
def get_active_regions(slf) ->list[str]:  
    cache_exists = False;
    if (cache_exists):
        path_to_data = "null"
        fetch_cached_data(path_to_data)
    else:     
        r = requests.get(f"{BASE_URL}/maps")
        r.raise_for_status()
        cache_valid_regions(r)
        return r.json()

#
def get_map_data() -> list[str]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
    cache_exists = False;
    if (cache_exists):
        path_to_data = "null"
        fetch_cached_data(path_to_data)
    else:
        r = requests.get(f"{BASE_URL}/maps/")
        r.raise_for_status()
        cache_map_data(r)
        return r.json()

def cache_map_data(requestData: dict | list) -> None:
    pass

def cache_valid_regions(requestData: dict | list) -> None:
    pass

def fetch_cached_data(path: str) -> dict | list:
    pass

data = get_map_data()
print(data)






# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")



#warData['winner']