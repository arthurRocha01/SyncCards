import requests

class AnkiService:
    def __init__(self, note, api_url='http://localhost:8765'):
        self.note = note
        self.api_url = api_url

    def add_note_to_anki(self):
        payload = {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": self.note
            }
        }
        response = requests.post(self.api_url, json=payload)
        print(f'response: {response.json()}')
        return response.json()