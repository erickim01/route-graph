import requests

### Wrapper to War API
#
# URL Construction
#
# Response Handling
#
# Static Caching

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"   #For now this goes to Able only

class FoxWarApiClient:
    def get_war_data(self):       #May be generalized in behavior later to allow GETs to Baker and Charlie
        r = requests.get(f"{BASE_URL}/war")
        r.raise_for_status()
        return r.json()

    #Returns Valid Regions
    def get_active_regions(self):       
        r = requests.get(f"{BASE_URL}/maps")
        r.raise_for_status()
        return r.json()

    def get_map_data(self):       #May be generalized in behavior later to allow GETs to Baker and Charlie
        r = requests.get(f"{BASE_URL}/maps/")
        r.raise_for_status()
        return r.json()


client = FoxWarApiClient()
data = client.get_map_data()
print(data)

# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")



#warData['winner']