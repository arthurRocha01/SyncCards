class NoteFactory:
    def __init__(self, data):
        self.data = data
        self.notes = []

    def create_notes(self):
        for item in self.data:
            self.notes.append(self._create_single_note(item))
        return self.notes

    def _create_single_note(self, note):
        return {
            'deckName': ...,
            'modelName': ...,
            'fields': {
                'Front': note.get('title', ''),
                'Back': note.get('answer', '')
            },
            'tags': []
        }