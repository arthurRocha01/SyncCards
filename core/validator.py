import re

REQUIRED_FIELDS = ["title", "answer"]
FORMAT_PATTERN = re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]')

class ValidatorHandler:
    def __init__(self, data):
        self.data = data
        self.errors = []
        self.questions_seen = set()
        self.answers_seen = set()

    def validate(self):
        valid_items = []
        for index, item in enumerate(self.data):
            item_errors = (
                self._missing_field(item) +
                self._empty_field(item) +
                self._invalid_type(item) +
                self._duplicate_question(item) +
                self._duplicate_answer(item) +
                self._format_issue(item)
            )

        if item_errors: self.errors.append( {'index': index, 'errors': item_errors} )
        else: valid_items.append(item)
        return valid_items

    def _missing_field(self, item):
        return [f'missing_field: {field}' for field in REQUIRED_FIELDS if field not in item]

    def _empty_field(self, item):
        return [f'empty_field: {field}' for field in REQUIRED_FIELDS if item.get(field, '').strip() == '']

    def _invalid_type(self, item):
        return [f'invalid_type: {field}' for field in REQUIRED_FIELDS if field in item and not isinstance(item[field], str)]

    def _duplicate_question(self, item):
        title = item.get('title')
        if title:
            if title in self.questions_seen: return ['duplicate_question']
            else: self.questions_seen.add(title)

    def _duplicate_answer(self, item):
        answer = item.get('answer')
        if answer:
            if answer in self.answers_seen: return ['duplicate_answer']
            else: self.answers_seen.add(answer)

    def _format_issue(self, item):
        return [f'format_issue: {field}' for field in REQUIRED_FIELDS if field in item and FORMAT_PATTERN.search(item[field])]