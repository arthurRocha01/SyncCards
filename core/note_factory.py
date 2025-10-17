class NoteFactory:
    def __init__(self, data):
        self.data = data
        self.notes = []

    def create_notes(self):
        for item in self.data:
            self.notes.append(self._create_single_note(item))
        return self.notes

    def _create_single_note(self, item):
        return {
            'deckName': 'Default',
            'modelName': 'Basic',
            'fields': {
                'Front': item.get('title', ''),
                'Back': item.get('answer', '')
            },
            'tags': []
        }