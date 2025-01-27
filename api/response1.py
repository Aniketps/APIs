import requests

response = requests.get("http://127.0.0.1:5000/greet")
if(response.status_code == 200):
    print(response.json())
    
print(response.status_code)