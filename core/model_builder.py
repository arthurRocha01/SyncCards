class ModelBuilder:
    def __init__(self, notes, logger):
        self.notes = notes
        self.logger = logger
        self.logger.info(f"ModelBuilder iniciado com {len(notes)} nota(s).")

    def build_models(self):
        """Cria todos os modelos de requisição para o AnkiConnect a partir das notas."""
        models = []
        for index, note in enumerate(self.notes):
            model = self._build_single_model(note)
            models.append(model)
            self.logger.debug(
                f"Modelo {index} criado para nota: Frente='{note['fields']['Frente']}', Verso='{note['fields']['Verso']}'"
            )
        
        self.logger.info(f"Total de {len(models)} modelo(s) criado(s).")
        self.logger.info(f"Modelos criados: {models}")
        return models

    def _build_single_model(self, note):
        """Constrói o JSON de requisição para uma única nota."""
        return {
            "action": "addNote",
            "version": 6,
            "params": {
                "note": note
            }
        }
