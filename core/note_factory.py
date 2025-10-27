class NoteFactory:
    def __init__(self, data_processed, logger):
        self.data_processed = data_processed
        self.logger = logger
        self.notes = []
        self.logger.info(f"NoteFactory iniciado com {len(data_processed)} item(s) processado(s).")

    def create_notes(self):
        """Cria todas as notas a partir dos dados processados."""
        for index, item in enumerate(self.data_processed):
            note = self._create_single_note(item)
            self.notes.append(note)
            self.logger.debug(f"Nota {index} criada: Frente='{note['fields']['Frente']}', Verso='{note['fields']['Verso']}'")
        
        self.logger.info(f"Total de {len(self.notes)} nota(s) criada(s).")
        self.logger.info(f"Notas criadas: {self.notes}")
        return self.notes

    def _create_single_note(self, item):
        """Cria uma nota individual para o Anki."""
        return {
            'deckName': 'teste',
            'modelName': 'Básico',
            'fields': {
                'Frente': item.get('frente', ''),
                'Verso': item.get('verso', '')
            },
            'tags': []
        }
