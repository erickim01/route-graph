import json                 #api_client.py imports 
import requests
import requests_cache
from typing import Any
from pathlib import Path    #end of api_client.py imports
#import null            #core.py imports

#######################
#---API_CLIENT WORK---#
#######################

### Wrapper to War API
#
# URL Construction
#
# Response Handling & Caching

#TODOTODOTODO: get_active_regions() - Implement New War Check.
#TODOTODOTODO: get_active_regions() - Build Path with current War number.

#TODOTODOTODO: get_map_data(region_name: str) - Implement error handle to ensure a valid region is selected, here or elsewhere

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"   #For now this goes to Able only
REGION_LIST_PATH = "regions_list.json"

def get_war_data() -> dict[str, Any]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
    r = requests.get(f"{BASE_URL}/war")
    r.raise_for_status()
    return r.json()

#Returns Valid Regions. Runs once per war to store regions active.
def get_active_regions() ->list[str]:  
    r = requests.get(f"{BASE_URL}/maps")            #TODOTODOTODO: Implement New War Check.
    r.raise_for_status()
    with open(REGION_LIST_PATH, "w") as f:         #TODOTODOTODO: Build Path with current War number.
        json.dump(r.json(), f)
    return r.json()

def fetch_cached_data(path: str) -> dict | list:
    with open(path, "r") as f:
        return json.load(f)

#User is presented with list of valid regions
#Selects ex. "The Fingers"
#Read into backend as "TheFingersHex"
#TODOTODOTODO: Implement error handle to ensure a valid region is selected, here or elsewhere
requests_cache.install_cache(
    cache_name='regions_cache',
    backend='sqlite',
    expire_after=None,
)

def get_map_data(region_name: str) -> list[str]:       
    r = requests.get(f"{BASE_URL}/maps/{region_name}/static") #Input Validation is assumed to be handled at this point
    r.raise_for_status()
    #cache_map_data(r)
    return r.json()

#Legacied if requests_cache is not desired or unable to be utilized.
# def cache_map_data(requestData: dict | list) -> None:
#     with open("map_data.json", "w") as f:
#         json.dump(requestData.json(), f)

############
#---CORE---#
############









############
#---CORE---#
############

# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")



#warData['winner']