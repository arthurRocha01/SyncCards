"""
Watcher de diretório usando watchdog.

Objetivo:
Monitorar a pasta ./inbox e processar automaticamente
arquivos recém-criados através da função process_file.

Componentes principais:
- Handler: define ação quando um arquivo é criado.
- start_watcher: inicia o observer e mantém a observação ativa.

Uso:
Chamando start_watcher(), o programa fica escutando
novos arquivos no diretório e processa cada um automaticamente.
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from service import process_file

# Caminho do diretório a ser monitorado
WATCH_PATH = "./inbox"

class Handler(FileSystemEventHandler):
    """
    Handler de eventos de sistema de arquivos.

    on_created:
    Chamado automaticamente quando um arquivo é criado.
    Ignora pastas e envia arquivos para a função process_file.
    """
    def on_created(self, event):
        if not event.is_directory:
            process_file(event.src_path)

def start_watcher():
    """
    Inicializa e inicia o watcher.

    1. Cria um Handler para eventos.
    2. Cria um Observer e conecta ao diretório WATCH_PATH.
    3. Inicia a observação em loop contínuo.
    4. Permite interrupção via Ctrl+C.
    """
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
