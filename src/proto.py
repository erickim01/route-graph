import json
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

#Returns Valid Regions. Runs once per war to store regions active.
def get_active_regions(slf) ->list[str]:  
    r = requests.get(f"{BASE_URL}/maps")            #TODOTODOTODO: Implement New War Check.
    r.raise_for_status()
    cache_valid_regions(r)
    return r.json()

def cache_valid_regions(requestData: dict | list) -> None:
    with open("regions_list.json()", "w") as f:         #TODOTODOTODO: Build Path with current War number.
        json.dump(requestData.json(), f)

def fetch_cached_data(path: str) -> dict | list:
    with open(path, "r") as f:
        return json.load(f)



#User is presented with list of valid regions
#Selects ex. "The Fingers"
#Read into backend as "TheFingersHex"
#Error handle to ensure a valid region is selected
#Path must GET with "TheFingersHex" and store in a similarly-named dump.
requests_cache.install_cache(
    cache_name='regions_cache',
    backend='sqlite',
    expire_after=None,
)

def get_map_data(REGION_NAME: str) -> list[str]:       
    r = requests.get(f"{BASE_URL}/maps/{REGION_NAME}/static") #Input Validation is assumed to be handled at this point
    r.raise_for_status()
    #cache_map_data(r)
    return r.json()

#Legacied if requests_cache is not desired or unable to be utilized.
# def cache_map_data(requestData: dict | list) -> None:
#     with open("map_data.json", "w") as f:
#         json.dump(requestData.json(), f)

# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")



#warData['winner']