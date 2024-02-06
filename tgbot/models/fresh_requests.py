from requests import post

fresh_service_key = 'mvRJlhX3GqC1PYmmAQQj'
fresh_service_domain = 'https://isyb.freshservice.com'


# def create_freshservice_ticket(subject, description):
#     url = '{0}/api/v2/tickets'.format(fresh_service_domain)
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Basic {}'.format(fresh_service_key)
#     }
#     data = {
#         'description': description,
#         'subject': subject,
#         'email': 'cacanj11@gmail.com',
#         'priority': 2
#     }
#     response = post(url=url, headers=headers, json=data)
#     if response.status_code == 201:
#         print(response)
#         return True
#     else:
#         print(response)
#         return False
        # FINISH


# if create_freshservice_ticket(subject='Its a test', description='something text'):
#     print("Good")
# else:
#     print("Not good")


# def create_freshservice_ticket(subject, description):
#     url = '{0}/api/v2/tickets'.format(fresh_service_domain)
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Basic {}'.format(fresh_service_key)
#     }
#     data = {
#         'description': description,
#         'subject': subject,
#         'email': 'my_qmail',
#         'priority': 2
#     }f
#
#     response = post(url=url, headers=headers, json=data)
#
#     if response.status_code == 201:
#         print("Ticket created successfully in Freshservice.")
#         return response.json()
#     elif response.status_code == 401:
#         print("Authentication error: Check your API key.")
#     else:
#         print("Failed to create a ticket in Freshservice. Status code:", response.status_code)
#         print("Response content:", response.text)
#
# # Пример использования функции
# ticket_data = create_freshservice_ticket('New Ticket from Python', 'This is a test ticket from Python.')
# if ticket_data:
#     print("Ticket ID:", ticket_data['id'])
#     print("Ticket URL:", ticket_data['helpdesk_ticket']['url'])
