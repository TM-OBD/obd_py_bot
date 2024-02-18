# from fastapi import FastAPI
# import json
# app = FastAPI()
#
# @app.post("/endpoint")
# async def handle_post_request(data: dict):
#
#     print(data)
#     with open("response.json", "a") as json_f:
#         json.dump(data, json_f)
#
#
#     return {"message": "POST request received"}
#
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="131.0.0.1", port=8000)
# uvicorn main:app --reload









#


import requests
from pprint import pprint


def req():
    params = {'q': 'python'}
    response = requests.get("https://api.github.com/search/repositories", params=params)
    return response

response = req()

if response.status_code == 200 or 201:
    pprint(response.text)
    # pprint(response.json()["items"][0]["description"])
else:
    pprint(response.status_code)
    pprint(response.text)


















