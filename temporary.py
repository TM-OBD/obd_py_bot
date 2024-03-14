# from requests import post
import json


# from time import sleep


class Temp_test:
    def __init__(self):
        pass

    @staticmethod
    def data_message(message):
        print('Message:\n{0}'.format(message))


# def sent_data_to_server():
    # server_url = ""
    # while True:
    #     try:
    #
    #         input_data = kwargs
    #
    #         response = post(url=server_url, json=input_data)
    #
    #         if response.status_code == 200:
    #             print("Success")
    #         else:
    #             print(f"Error, file is ???, code:{response.status_code}\ntext: {response.text}")
    #
    #         sleep(seconds=10)
    #
    #     except Exception as e:
    #         print(f"Error, file is ???, code:{e}")
    # with open("input_data.json", "r+") as file:
    #     data = json.load(file)
    # with open("input_data.json", "w") as file:
    #     json.dump({}, file)


# sent_data_to_server()
