import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from service import ServiceHandler
from logger import logger

WATCH_PATH = "~/anki-flashcards"

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.service = ServiceHandler()
        self.files_to_process = []

    def process_two_files(self):
        files_pair = self.files_to_process[:2]
        logger.info(f"Arquivos dectados: {files_pair[0]}, {files_pair[1]}")
        self.service.process_file(files_pair)
        self.files_to_process = self.files_to_process[2:]

    def on_created(self, event):
        if not event.is_directory:
            self.files_to_process.append(event.src_path)
            if len(self.files_to_process) == 2:
                self.process_two_files()


    def start_watcher():
        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, WATCH_PATH, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()