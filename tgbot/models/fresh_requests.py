from requests import post

#Marco Q1BAynlmwvAIiW78nv4S
# fresh_service_key = "5FHn7ZAr5rP91KrKg6Tu"
# fresh_service_domain = "https://isyb.freshservice.com"

url = "https://isyb.freshservice.com/api/v2/tickets"
api_key = 'Q1BAynlmwvAIiW78nv4S'

headers = {
    'Content-Type': 'application/json'
}

data = {
    "description": "Details about the issue...",
    "subject": "Support",
    "email": "cacanj11@gmail.com",
    "status": 2,
    "priority": 1
}

response = post(url, headers=headers, json=data, auth=('Q1BAynlmwvAIiW78nv4S', 'X'))
print(response.status_code)
print(response.text)
# headers = {
#     "Content-Type": "application/json",
#
# }
# data = {
#     "description": "Its a test request",
#     "subject": "Test",
#     "email": "cacanj11@gmail.com",
#     "priority": 1,
#     "status": 2
# }
#
# response = post(url=url, headers=headers, json=data, auth=('api_key', 'X'))

# if response.status_code == 201:
#     print("Service request created successfully in Freshservice.")
#     print("Service Request ID:", response.json()['service_request']['id'])
#     print(response)
# else:
#     print("Failed to create a ticket in Freshservice. Status code:", response.status_code)
#     print("Response content:", response.text)
#     print(response)
#
















