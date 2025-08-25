import os
import base64
import requests
from logger import logger

ANKI_URL = "http://127.0.0.1:8765"

class AnkiClientHandler:
    def request(self, action: str, **params):
        payload = {"action": action, "version": 6, "params": params}
        response = requests.post(ANKI_URL, json=payload)
        response.raise_for_status()
        return response.json()

    def _encode_file(self, path: str) -> str:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def send_to_anki(self, image_front: str, image_back: str):
        front_name = os.path.basename(image_front)
        back_name = os.path.basename(image_back)

        for path, name in [(image_front, front_name), (image_back, back_name)]:
            self.request("storeMediaFile", filename=name, data=self._encode_file(path))

        note = {
            "deckName": "Default",
            "modelName": "Basic",
            "fields": {
                "Front": f"<img src='{front_name}'>",
                "Back": f"<img src='{back_name}'>",
            },
            "options": {"allowDuplicate": False},
            "tags": ["auto"],
        }

        result = self.request("addNote", note=note)
        if "error" in result and result["error"]:
            logger.error(f"Erro ao enviar note: {result['error']}")
        else:
            logger.info(f"Flashcard enviado: {front_name} | {back_name}")
        print(result)