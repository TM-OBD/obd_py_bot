from requests import post, get


url = "https://isyb.freshservice.com/api/v2/tickets/20"
api_key = 'Q1BAynlmwvAIiW78nv4S'

headers = {
    'Content-Type': 'application/json'
}

response = get(url, headers=headers, auth=('Q1BAynlmwvAIiW78nv4S', 'X'))


if response.status_code == 200:
    notes = response.json()
    print(notes)
    # for note in notes:
    #     print(f"Author: {note['user']['name']}")
    #     print(f"Body: {note['body']}")
    #     print(f"Created at: {note['created_at']}")
    #     print("---------------")
else:
    print("Failed to retrieve ticket notes. Status code:", response.status_code)
    print("Response content:", response.text)

# {'ticket':
# {'subject': 'SoS', 'group_id': None, 'department_id': None, 'category': None, 'sub_category': None, 'item_category': None, 'requester_id': 54001538979,
# 'responder_id': 54001520365, 'due_by': '2024-03-01T22:00:00Z', 'fr_escalated': False, 'deleted': False, 'spam': False, 'email_config_id': None, 'fwd_emails': [],
# 'reply_cc_emails': [], 'cc_emails': [], 'is_escalated': False, 'fr_due_by': '2024-02-23T19:00:00Z', 'id': 20, 'priority': 1, 'status': 2, 'source': 1001, 'created_at': '2024-02-20T17:32:58Z',
# 'updated_at': '2024-02-20T17:35:50Z', 'requested_for_id': 54001538979, 'to_emails': None, 'type': 'Incident', 'description': '<div>Details about the issue lol</div>', 'description_text': 'Details about the issue lol', 'custom_fields': {'major_incident_type': None, 'business_impact': None, 'impacted_locations': None, 'no_of_customers_impacted': None}, 'workspace_id': 2, 'sla_policy_id': 54000036590, 'impact': 1, 'urgency': 1, 'bcc_emails': None, 'applied_business_hours': 54000006639, 'created_within_business_hours': False, 'resolution_notes': None, 'resolution_notes_html': None, 'attachments': []}}



