import requests

response = requests.get("https://aniketapi.ancientcoders.in/greet")
if(response.status_code == 200):
    print(response.json())
    
print(response.status_code)