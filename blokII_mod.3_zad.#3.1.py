import os
from threading import Thread
import logging
from collections import defaultdict

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Funkcja do sortowania plików według rozszerzeń
def sort_files_by_extension(folder_path):
    logging.info(f"Started sorting files in folder: {folder_path}")
    extensions = defaultdict(list)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]
            extensions[file_extension].append(file_path)

    logging.info(f"Folder processing completed: {folder_path}")
    return extensions

# Funkcja wykonująca przetwarzanie dla każdego folderu w osobnym wątku
def process_folders_in_threads(folder_path):
    threads = []
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            thread = Thread(target=sort_files_by_extension, args=(dir_path,))
            threads.append(thread)
            thread.start()
            logging.info(f"Started sorting files in folder: {dir_path}")

    for thread in threads:
        thread.join()
        logging.info(f"Folder processing completed: {dir_path}")

# Przykładowe użycie
if __name__ == "__main__":
    folder_to_sort = r"C:\Users\MD\Documents\Bałagan"  # Wpisz ścieżkę do folderu

    # uruchomienie funkcji 
    process_folders_in_threads(folder_to_sort)
