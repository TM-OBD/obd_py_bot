import json

with open("response.json", "r") as f:
    json_data = json.load(f)
print(json_data)