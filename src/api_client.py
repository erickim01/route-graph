import requests
from typing import Any

### Wrapper to War API
#
# URL Construction
#
# Response Handling
#
# Static Caching

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"   #For now this goes to Able only

class FoxWarApiClient:
    def get_war_data(self) -> dict[str, Any]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
        r = requests.get(f"{BASE_URL}/war")
        r.raise_for_status()
        return r.json()

    #Returns Valid Regions
    def get_active_regions(self) ->list[str]:       
        r = requests.get(f"{BASE_URL}/maps")
        r.raise_for_status()
        return r.json()

    def get_map_data(self, requested_map_name: str) -> list[str]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
        r = requests.get(f"{BASE_URL}/maps/{requested_map_name}/static")
        r.raise_for_status()
        return r.json()   
    
    #:mapName/static
    



client = FoxWarApiClient()
data = client.get_map_data("TheFingersHex")
print(data)

# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")



#warData['winner']