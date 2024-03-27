from requests import post, get
from json import loads


# Marco Q1BAynlmwvAIiW78nv4S


class FreshServiceRequests:
    """All interactions with the freshservice"""
    __api_token = 'Q1BAynlmwvAIiW78nv4S'

    def create_ticket(self, subject: str, description: str):
        """Функия для создания tikcet"""
        __url_create = "https://isyb.freshservice.com/api/v2/tickets"
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            "description": description,
            "subject": subject,
            "email": "cacanj14@gmail.com",
            "status": 2,
            "priority": 1,
            "source": 1001
        }

        response = post(url=__url_create, headers=headers, json=data, auth=(self.__api_token, 'X'))

        if response.status_code == 201:
            print("Service request created successfully in Freshservice.")
            print(response.text)
            id_ticket = response.json()["ticket"]["id"]
            # сохранение данных
        else:
            print("Failed to create a ticket in Freshservice. Status code:", response.status_code)
            print("Response content:", response.text)

    def get_ticket(self, user_id: int = 48):
        """Функия для получения ответа на tikcet"""
        # requests to database for ticket id
        ticket_id = user_id
        headers = {
            'Content-Type': 'application/json'
        }
        url = f"https://isyb.freshservice.com/api/v2/tickets/{ticket_id}?include=conversations"
        response_get = get(url, headers=headers, auth=(self.__api_token, 'X'), json=True)

        print(response_get.status_code)

        d = loads(response_get.text)
        # print(d["ticket"]["conversations"][0]["body_text"])
        print(d)

    def service_ticket(self, description: str = None, subject: str = None):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "description": description,
            "subject": subject,
            "email": "cacanj14@gmail.com",
            "status": 2,
            "priority": 1,
            "source": 1001
        }
        url = "https://isyb.freshservice.com/api/v2/service_catalog/items/26/place_request"

        response = post(url=url, headers=headers, auth=(self.__api_token, 'X'), json=data)

        if response.status_code == 201:
            print("Service request created successfully in Freshservice.")
            print(response.text)
        else:
            print("Failed to create a ticket in Freshservice. Status code:", response.status_code)
            print("Response content:", response.text)

    def get_service_items(self):

        url = "https://isyb.freshservice.com/api/v2/tickets/52/requested_items"

        response = get(url, auth=(self.__api_token, 'X'), json=True)

        print(response.status_code)
        print(response.text)

    # def check_phone(self, phone: str = None):
    #     headers = {
    #         'Content-Type': 'application/json'
    #     }
    #     url = ""
    #
    #     data = {1: "one"}
    #
    #     response = post(url=url, headers=headers, json=data, auth=(self.__api_token, 'X'))
    #
    #     if response.status_code == 201:
    #         print("Service request created successfully in Freshservice.")
    #         print(response.text)
    #     else:
    #         print("Failed to create a ticket in Freshservice. Status code:", response.status_code)
    #         print("Response content:", response.text)
    #

# d = {"ticket":{"subject":"TestTrecker 2","group_id": None,"department_id":None,"category":None,"sub_category":None,"item_category":None,"requester_id":54001538979,"responder_id":54001520365,"due_by":"2024-03-01T22:00:00Z","fr_escalated":False,"deleted":False,"spam":False,"email_config_id":None,"fwd_emails":[],"reply_cc_emails":[],"cc_emails":[],"is_escalated":True,"fr_due_by":"2024-02-23T19:00:00Z","id":34,"priority":1,"status":2,"source":1,"created_at":"2024-02-20T17:48:22Z","updated_at":"2024-02-20T17:48:52Z","requested_for_id":54001538979,"to_emails":["marcoukhanov.ca@gmail.com"],"type":"Incident","description":"<div dir=\"ltr\"><br></div>\n\n","description_text":"","custom_fields":{"major_incident_type":None,"business_impact":None,"impacted_locations":None,"no_of_customers_impacted":None},"workspace_id":2,"sla_policy_id":54000036590,"impact":1,"urgency":1,"conversations":[{"id":54002047643,"body":"<div style=\"font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif; font-size: 14px; \"><div dir=\"ltr\">Hi test reply</div></div>","incoming":False,"private":False,"created_at":"2024-02-20T17:48:51Z","updated_at":"2024-02-20T17:48:51Z","user_id":54001520365,"source":0,"cc_emails":[],"from_email":"gmail <marcoukhanov.ca@gmail.com>","to_emails":["cacanj14@gmail.com"],"bcc_emails":[],"attachments":[],"ticket_id":34,"body_text":"Hi test reply","support_email":"marcoukhanov.ca@gmail.com"}],"bcc_emails":[],"applied_business_hours":54000006639,"created_within_business_hours":False,"resolution_notes":None,"resolution_notes_html":None,"attachments":[]}}
# {'ticket': {'subject': 'TestTrecker 2', 'group_id': None, 'department_id': None, 'category': None, 'sub_category': None, 'item_category': None, 'requester_id': 54001538979, 'responder_id': 54001520365, 'due_by': '2024-03-01T22:00:00Z', 'fr_escalated': False, 'deleted': False, 'spam': False, 'email_config_id': None, 'fwd_emails': [], 'reply_cc_emails': [], 'cc_emails': [], 'is_escalated': True, 'fr_due_by': '2024-02-23T19:00:00Z', 'id': 34, 'priority': 1, 'status': 2, 'source': 1, 'created_at': '2024-02-20T17:48:22Z', 'updated_at': '2024-03-18T16:44:42Z', 'requested_for_id': 54001538979, 'to_emails': ['marcoukhanov.ca@gmail.com'], 'type': 'Incident', 'description': '<div dir="ltr"><br></div>\n\n', 'description_text': '', 'custom_fields': {}, 'workspace_id': 2, 'sla_policy_id': 54000036590, 'impact': 1, 'urgency': 1, 'conversations': [{'id': 54002047643, 'body': '<div style="font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif; font-size: 14px; "><div dir="ltr">Hi test reply</div></div>', 'incoming': False, 'private': False, 'created_at': '2024-02-20T17:48:51Z', 'updated_at': '2024-02-20T17:48:51Z', 'user_id': 54001520365, 'source': 0, 'cc_emails': [], 'from_email': 'gmail <marcoukhanov.ca@gmail.com>', 'to_emails': ['cacanj14@gmail.com'], 'bcc_emails': [], 'attachments': [], 'ticket_id': 34, 'body_text': 'Hi test reply', 'support_email': 'marcoukhanov.ca@gmail.com'}, {'id': 54002448090, 'body': '<div style="font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif; font-size: 14px; "><div>Hi Trecker Trecker,<br><br>Ticket: <a href="https://isyb.freshservice.com/helpdesk/tickets/34" rel="noreferrer">https://isyb.freshservice.com/helpdesk/tickets/34</a></div></div>', 'incoming': False, 'private': False, 'created_at': '2024-03-18T16:44:42Z', 'updated_at': '2024-03-18T16:44:42Z', 'user_id': 54001520365, 'source': 0, 'cc_emails': [], 'from_email': 'Support <support@isyb.com.ua>', 'to_emails': ['cacanj14@gmail.com'], 'bcc_emails': [], 'attachments': [], 'ticket_id': 34, 'body_text': 'Hi Trecker Trecker,  Ticket: https://isyb.freshservice.com/helpdesk/tickets/34', 'support_email': 'support@isyb.com.ua'}], 'bcc_emails': [], 'applied_business_hours': 54000006639, 'created_within_business_hours': False, 'resolution_notes': None, 'resolution_notes_html': None, 'attachments': []}}
# 52

# my_data = {
#     "description": "Details about the issue lol",
#     "subject": "SoS",
#     "email": "cacanj14@gmail.com",
#     "status": 2,
#     "priority": 1,
#     "source": 1001
# }

# c = FreshServiceRequests()
#
# c.check_phone("+380662087657")
# +380662087657
