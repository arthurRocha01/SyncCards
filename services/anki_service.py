import requests

class AnkiService:
    def __init__(self, models, logger, api_url='http://localhost:8765'):
        self.models = models
        self.logger = logger
        self.api_url = api_url
        self.logger.info(f"AnkiService iniciado com {len(models)} modelo(s).")

    def add_models_to_anki(self):
        """Envia todos os modelos para o AnkiConnect."""
        total = len(self.models)
        self.logger.info(f"Iniciando envio de {total} modelo(s) para o AnkiConnect.")

        results = []
        for index, model in enumerate(self.models):
            self.logger.debug(f"Enviando modelo {index + 1}/{total}: {model}")
            response = self._add_single_model_to_anki(model)
            results.append(response)
            self.logger.debug(f"Resposta do modelo {index + 1}: {response}")

        self.logger.info(f"Envio concluído. {len(results)} resposta(s) recebida(s).")
        self.logger.info(f"Resultados finais: {results}")
        return results

    def _add_single_model_to_anki(self, model):
        """Envia um único modelo para o AnkiConnect."""
        return self._handle_response(model)

    def _handle_response(self, payload):
        """Realiza o POST e trata a resposta do AnkiConnect."""
        try:
            self.logger.debug(f"POST para {self.api_url} com payload: {payload}")
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            response_data = response.json()
            self.logger.info(f"Resposta do AnkiConnect recebida: {response_data}")
            return response_data
        except requests.RequestException as e:
            self.logger.error(f"Erro ao enviar modelo para AnkiConnect: {e}")
            return {"error": str(e)}
        except ValueError as e:
            self.logger.error(f"Erro ao decodificar resposta JSON: {e}")
            return {"error": "Resposta inválida do AnkiConnect"}
