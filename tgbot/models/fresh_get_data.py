from requests import post


url = "https://isyb.freshservice.com/api/v2/tickets/11/notes"
api_key = 'Q1BAynlmwvAIiW78nv4S'

headers = {
    'Content-Type': 'application/json'
}


response = post(url, headers=headers, auth=('Q1BAynlmwvAIiW78nv4S', 'X'))

if response.status_code == 200:
    notes = response.json()

    for note in notes:
        print(f"Author: {note['user']['name']}")
        print(f"Body: {note['body']}")
        print(f"Created at: {note['created_at']}")
        print("---------------")
else:
    print("Failed to retrieve ticket notes. Status code:", response.status_code)
    print("Response content:", response.text)