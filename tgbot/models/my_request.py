from requests import post
from dataclasses import dataclass


@dataclass
class Request:
    url: str
    data: any

    def req_post(self) -> None:
        response = post(url=self.url, json=self.data)

        print("Status code: {}".format(response.status_code))
        print("Response: {}".format(response.text))

while True:
    if int(input()) == 1:
        Request(url="http://127.0.0.1:8000/endpoint", data={"user_id": 1234, "firstname": "Alex"}).req_post()
    else:
        break
