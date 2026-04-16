import requests

BASE_URL = "https://war-service-live.foxholeservices.com/api"

print(requests.get(f"{BASE_URL}/worldconquest/war").json())