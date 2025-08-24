import os
from anki_client import send_to_anki

def process_file(path):
    """
    Processa um arquivo de flashcard e envia para o Anki se o par existir.

    Padrão esperado:
        - Frente: <nome>_front.ext
        - Verso:  <nome>_back.ext

    Parâmetros:
        path (str): Caminho completo do arquivo.

    Comportamento:
        - Identifica se o arquivo é front ou back.
        - Procura o arquivo complementar no mesmo diretório.
        - Se ambos existirem, chama send_to_anki(front, back).
    """
    base, fname = os.path.split(path)

    if "_front" in fname:
        back_file = fname.replace("_front", "_back")
    elif "_back" in fname:
        back_file = fname.replace("_back", "_front")
    else:
        return

    pair_path = os.path.join(base, back_file)

    if os.path.exists(pair_path):
        print(f"[+] Par encontrado: {fname} e {back_file}")
        send_to_anki(path, pair_path)