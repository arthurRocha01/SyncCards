import re

REQUIRED_FIELDS = ["front", "back"]
FORMAT_PATTERN = re.compile(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]')

class ProcessorHandler:
    def __init__(self, data, logger):
        self.data = data
        self.logger = logger
        self.errors = []
        self.questions_seen = set()
        self.answers_seen = set()
        self.logger.info(f"Processador iniciado com {len(data)} item(s).")

    def process(self):
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

            if item_errors:
                self.errors.append({'index': index, 'errors': item_errors})
                self.logger.warning(f"Item {index} com erros: {item_errors}")
            else:
                valid_items.append(item)

        # Log final resumido
        self.logger.info(f"Processamento concluído: {len(valid_items)} item(s) válidos, {len(self.errors)} item(s) com erros.")
        self.logger.info(f"Itens processados: {valid_items}")

        return valid_items

    def _missing_field(self, item):
        return [f'missing_field: {field}' for field in REQUIRED_FIELDS if field not in item]

    def _empty_field(self, item):
        return [f'empty_field: {field}' for field in REQUIRED_FIELDS if item.get(field, '').strip() == '']

    def _invalid_type(self, item):
        return [f'invalid_type: {field}' for field in REQUIRED_FIELDS if field in item and not isinstance(item[field], str)]

    def _duplicate_question(self, item):
        front = item.get('front')
        if front:
            if front in self.questions_seen: 
                return ['duplicate_question']
            else: 
                self.questions_seen.add(front)
        return []

    def _duplicate_answer(self, item):
        back = item.get('back')
        if back:
            if back in self.answers_seen: 
                return ['duplicate_answer']
            else: 
                self.answers_seen.add(back)
        return []

    def _format_issue(self, item):
        return [f'format_issue: {field}' for field in REQUIRED_FIELDS if field in item and FORMAT_PATTERN.search(item[field])]