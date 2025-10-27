import logging

class Logger:
    def __init__(self, filename='logs/synccards.log', level=logging.DEBUG):
        self.logger = logging.getLogger('SyncCardsLogger')
        self.logger.setLevel(level)

        if not self.logger.hasHandlers():
            self._create_file_handler(filename, level)

    def _create_file_handler(self, filename, level):
        if not self.logger.hasHandlers():
            handler = logging.FileHandler(filename)
            handler.setLevel(level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter) 
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
