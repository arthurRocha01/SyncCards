import requests
import os

ANKI_URL = "http://127.0.0.1:8765"

def request(action, **params):
    """
    Envia uma requisição para o AnkiConnect.

    Parâmetros:
        action (str): Ação a ser executada na API (ex: "addNote", "storeMediaFile").
        **params: Parâmetros específicos da ação.

    Retorno:
        dict: Resposta JSON da API do Anki.
    """
    return requests.post(
        ANKI_URL, 
        json={"action": action, "version": 6, "params": params}
    ).json()

def send_to_anki(front, back):
    """
    Envia um par de imagens para o Anki e cria um flashcard.

    Padrão esperado de arquivos:
        - Frente: <nome>_front.ext
        - Verso:  <nome>_back.ext

    Parâmetros:
        front (str): Caminho completo da imagem da frente.
        back (str): Caminho completo da imagem do verso.

    Comportamento:
        1. Envia as imagens para o Anki usando "storeMediaFile".
        2. Cria um flashcard do tipo "Basic" no deck "Default" com as imagens.
        3. Evita duplicatas e adiciona a tag "auto".
        4. Imprime o resultado da operação.
    """
    front_name = os.path.basename(front)
    back_name = os.path.basename(back)

    for file in [front, back]:
        request(
            "storeMediaFile",
            filename=os.path.basename(file),
            data=open(file, "rb").read().decode("latin1")
        )

    note = {
        "deckName": "Default",
        "modelName": "Basic",
        "fields": {
            "Front": f"<img src='{front_name}'>",
            "Back": f"<img src='{back_name}'>"
        },
        "options": {"allowDuplicate": False},
        "tags": ["auto"]
    }

    result = request("addNote", note=note)
    print("Enviado:", result)