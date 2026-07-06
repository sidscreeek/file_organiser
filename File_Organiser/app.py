import os 
import shutil

folder_path = "Downloads"
summary = {}

categories = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".sql", ".json", ".md"],
    "Data": [".csv", ".xlsx", ".xls"],
}
#loop through every file in the downlaods folder 
for file in os.listdir(folder_path):

    source_path=os.path.join(folder_path,file)

    #if it is a folder then continue 
    if os.path.isdir(source_path):
        continue

    extention = os.path.splitext(file)[1].lower()

    #default category = "Others"

    destination_folder="Others"

    for category,extentions in categories.items():
        if extention in extentions:
            destination_folder=category
            break

    destination_path = os.path.join(folder_path,destination_folder)
    os.makedirs(destination_path, exist_ok=True) #will make a folder if dosent exist 


    destination_file = os.path.join(destination_path,file)

    if os.path.exists(destination_file):
        filename,ext = os.path.splitext(file)
        counter=1

        while True:
            new_name=f"{filename}_{counter}{ext}"
            destination_file = os.path.join(destination_path,new_name)

            if not os.path.exists(destination_file):
                break
            counter+=1;

    shutil.move(source_path, destination_file)
    summary[destination_folder] = summary.get(destination_folder,0)+1

print(f"files organised successfully")
total=0

for category,count in summary.items():
    print(f"{category:<12} : {count}")
    total+=count

print("-"*25)
print(f"Total:{total}")


