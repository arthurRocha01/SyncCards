from core.logger import Logger
from core.input_handler import InputHandler
from core.processor import ProcessorHandler
from core.note_factory import NoteFactory
from core.model_builder import ModelBuilder
from services.anki_service import AnkiService

def main():
    logger_instance = Logger()
    logger = logger_instance.get_logger()
    print('Iniciando o processo de importação de notas.\n')

    input_handler = InputHandler(logger)
    data = input_handler.collect()
    print(f'Dados coletados: {data}\n')

    processor_handler = ProcessorHandler(data, logger)
    data_processed = processor_handler.process()
    print(f'Dados processados: {data_processed}\n')

    notes_handler = NoteFactory(data_processed, logger)
    notes = notes_handler.create_notes()
    print(f'Notas criadas: {notes}\n')

    model_builder = ModelBuilder(notes, logger)
    models = model_builder.build_models()
    print(f'Modelos construídos: {models}\n')

    anki_service = AnkiService(models, logger, 'http://127.0.0.1:5000/test')
    responses = anki_service.add_models_to_anki()
    print(f'Respostas do AnkiConnect: {responses}\n')
    
if __name__ == '__main__':
    main()