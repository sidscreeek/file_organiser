import os 

base_folder = "Downloads"

files = [
    "Resume.pdf",
    "Invoice.pdf",
    "Budget.xlsx",
    "vacation.jpg",
    "birthday.png",
    "notes.txt",
    "Project.docx",
    "Presentation.pptx",
    "movie.mp4",
    "song.mp3",
    "archive.zip",
    "source.rar",
    "main.py",
    "app.js",
    "data.csv",
    "README.md",
    "logo.svg",
    "wallpaper.webp",
    "database.sql",
    "report.pdf",
    "assignment.docx",
    "screenshot.png",
    "audio.wav",
    "video.mov",
    "script.py",
    "style.css",
    "unknown.xyz",
    "temp.tmp",
    "backup.tar.gz"
]

os.makedirs(base_folder, exist_ok=True)
for file in files:
    path = os.path.join(base_folder,file)
    with open(path, "w") as f:
        f.write(f"this is a file named {file}")

print("Dataset created successfully!!!")
