import json
from pathlib import Path

DEFAULT_TEMPLATE = [
    {"frente": "...", "verso": "..."}
]

class InputHandler:
    def __init__(self, logger, filepath='input/data.json', template=None):
        self.logger = logger
        self.filepath = Path(filepath)
        self.template = template or DEFAULT_TEMPLATE
        self.logger.info(f"InputHandler iniciado com filepath={self.filepath}")

    def collect(self):
        """Garante que o arquivo existe e retorna os dados do JSON."""
        self._ensure_file_exists()
        data = self._read_file()
        self.logger.info(f'Arquivo {self.filepath} lido com sucesso. {len(data)} item(s) carregado(s).')
        self.logger.info(f'Dados coletados: {data}')
        return data

    def _ensure_file_exists(self):
        """Cria o arquivo com o template padrão se não existir ou estiver vazio."""
        if not self.filepath.exists() or self.filepath.stat().st_size == 0:
            if not self.filepath.exists():
                self.logger.warning(f"Arquivo {self.filepath} não existe. Criando com template padrão...")
            else:
                self.logger.warning(f"Arquivo {self.filepath} está vazio. Inserindo template padrão...")

            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            self._write_json(self.template)
            self.logger.info(f'Arquivo {self.filepath} criado com o template padrão.')

    def _write_json(self, data):
        """Escreve dados em JSON no arquivo com formatação legível."""
        try:
            self.filepath.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding='utf-8')
        except Exception as e:
            self.logger.error(f'Erro ao escrever arquivo {self.filepath}: {e}')
            raise

    def _read_file(self):
        """Lê o arquivo JSON e valida se é uma lista de objetos."""
        try:
            data = json.loads(self.filepath.read_text(encoding='utf-8'))
        except json.JSONDecodeError as error:
            self.logger.error(f'Erro ao ler json: {error}')
            raise ValueError(f'Erro ao ler json: {error}')
        except Exception as e:
            self.logger.error(f'Erro inesperado ao ler arquivo {self.filepath}: {e}')
            raise

        if not isinstance(data, list):
            self.logger.error('O arquivo JSON deve conter uma lista de objetos.')
            raise ValueError('O arquivo JSON deve conter uma lista de objetos.')

        return data
