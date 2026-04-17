import requests

### Wrapper to War API
#
# URL Construction
#
# Response Handling
#
# Static Caching

BASE_URL = "https://war-service-live.foxholeservices.com/api/worldconquest"   #For now this goes to Able only

def getWarData():       #May be generalized in behavior later to allow GETs to Baker and Charlie
    r = requests.get(f"{BASE_URL}/war")
    r.raise_for_status()
    return r.json()

#Returns Valid Regions
def getActiveRegions():       
    r = requests.get(f"{BASE_URL}/maps")
    r.raise_for_status()
    return r.json()

def getMapData():       #May be generalized in behavior later to allow GETs to Baker and Charlie
    r = requests.get(f"{BASE_URL}/maps/")
    r.raise_for_status()
    return r.json()


data = getMapData()

# for key, value in data.items():
#     print(f"{key}   -    Value: {value}")

print(data)

#warData['winner']