from core.input_handler import InputHandler
from core.processor import ProcessorHandler
from core.note_factory import NoteFactory
from services.anki_service import AnkiService
from core.logger import Logger

def main():
    logger = Logger().get_logger()
    input_handler = InputHandler('input_data.json')
    processor_handler = ProcessorHandler(input_handler)
    notes_handler = NoteFactory(processor_handler)
    anki_service = AnkiService(notes_handler).add_note_to_anki()