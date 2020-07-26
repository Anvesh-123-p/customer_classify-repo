
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Annual Income':2, 'Spending Score':9})

print(r.json())
