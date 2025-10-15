import json
from pathlib import Path

DEFAULT_TEMPLATE = [
    {"titulo": "Exemplo de pergunta", "resposta": "Exemplo de resposta", "tags": ["exemplo"]}
]

class InputHandler:
    def __init__(self, filepath='input/data.json', template=None):
        self.filepath = Path(filepath)
        self.template = template or DEFAULT_TEMPLATE

    def collect(self):
        """Garante que o arquivo existe e retorna os dados do JSON."""
        self._ensure_file_exists()
        return self._read_file()

    def _ensure_file_exists(self):
        """Cria o arquivo com o template padrão se não existir."""
        if not self.filepath.exists():
            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            self._write_json(self.template)
            print(f'Arquivo {self.filepath} criado com o template padrão.')

    def _write_json(self, data):
        """Escreve dados em JSON no arquivo com formatação legível."""
        self.filepath.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding='utf-8')


    def _read_file(self):
        """Lê o arquivo JSON e valida se é uma lista de objetos."""
        try:
            data = json.loads(self.filepath.read_text(encoding='utf-8'))
        except json.JSONDecodeError as error:
            raise ValueError(f'Erro ao ler json: {error}')

        if not isinstance(data, list):
            raise ValueError('O arquivo JSON deve conter uma lista de objetos.')
        
        return data