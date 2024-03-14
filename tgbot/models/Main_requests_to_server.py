from dataclasses import dataclass
from json import dump, load
from time import sleep
from requests import post


class Connect:
    pass


@dataclass
class MainRequests(Connect):
    stop: str = None
    _data: dict = None
    __server_url: str = ""

    def write_to_file(self) -> None:
        with open("files/input_data.json", "a") as file:
            dump(self._data, file)

    def sent_to_server(self) -> None:
        # while True:
        try:
            with open("input_data.json", "r") as file:
                __data_f = load(file)

            response = post(url=self.__server_url, json=__data_f)
            # if response.status_code == 200:
            #     print("Success")
            # else:
            #     print(f"Error, file is ???, code:{response.status_code}\ntext: {response.text}")
            with open("input_data.json", "w") as file:
                dump({}, file)
            sleep(seconds=20)

        except Exception as e:
            print(f"Error, text: {e}")

                # for key, value in data_f.items():
                #     print(key)
                #     print(value[0])

    @staticmethod
    def is_authorized():
        pass

    @staticmethod
    def is_client():
        pass

    @staticmethod
    def authorization():
        pass


# dat = {
#     "access": [
#         "switchport mode access",
#         "switchport access vlan",
#         "switchport nonegotiate",
#         "spanning-tree portfast",
#         "spanning-tree bpduguard enable"
#     ],
#     "trunk": [
#         "switchport trunk encapsulation dot1q",
#         "switchport mode trunk",
#         "switchport trunk native vlan 999",
#         "switchport trunk allowed vlan"
#     ]
# }

# MainRequests().sent_to_server()