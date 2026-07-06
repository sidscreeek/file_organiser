import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_path = "Downloads"

categories = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".sql", ".json", ".md"],
    "Data": [".csv", ".xlsx", ".xls"],
}

def organize_file(source_path):
    file = os.path.basename(source_path)

    if os.path.isdir(source_path) or not os.path.exists(source_path):
        return

    extention = os.path.splitext(file)[1].lower()
    destination_folder = "Others"

    for category, extentions in categories.items():
        if extention in extentions:
            destination_folder = category
            break

    destination_path = os.path.join(folder_path, destination_folder)
    os.makedirs(destination_path, exist_ok=True)

    destination_file = os.path.join(destination_path, file)

    if os.path.exists(destination_file):
        filename, ext = os.path.splitext(file)
        counter = 1
        while True:
            new_name = f"{filename}_{counter}{ext}"
            destination_file = os.path.join(destination_path, new_name)
            if not os.path.exists(destination_file):
                break
            counter += 1

    shutil.move(source_path, destination_file)
    print(f"Moved: {file} -> {destination_folder}")


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(0.5)
            organize_file(event.src_path)


if __name__ == "__main__":
    observer = Observer()
    handler = Handler()
    observer.schedule(handler, folder_path, recursive=False)
    observer.start()
    print(f"Watching '{folder_path}' for new files... (Ctrl+C to stop)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching.")
    observer.join()