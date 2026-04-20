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
    def __init__(self):
        self.session = requests.Session()
        
    def get_war_data(self) -> dict[str, Any]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
        r = requests.get(f"{BASE_URL}/war")
        r.raise_for_status()
        return r.json()

    #Returns Valid Regions
    def get_active_regions(self) ->list[str]:  
        if (True):     #If the list is not yet cached
            r = requests.get(f"{BASE_URL}/maps")
            r.raise_for_status()
            return r.json()
        
    
    def fetch_active_regions(self):     #Fetches map active regions via cached.
        pass


    def get_map_data(self, requested_map_name: str) -> list[str]:       #May be generalized in behavior later to allow GETs to Baker and Charlie
        #CHECK if map data is cached. 
        if (1 == 0):    ##IF isCached:
            pass#return the contents of the region cache.
             
        r = requests.get(f"{BASE_URL}/maps/{requested_map_name}/static")
        r.raise_for_status()
        #Write to cache
        return r.json()   
    
    #:mapName/static
