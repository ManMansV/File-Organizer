import os
import shutil

def organize(folder):
    files = os.listdir(folder)
    for f in files:
        if not os.path.isfile(os.path.join(folder, f)):
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext in [".png", ".jpg", ".jpeg", ".gif"]:
            dest_folders = "Images"
        elif ext in [".pdf", ".txt", ".docx"]:
            dest_folders = "Documents"
        elif ext in [".py", ".js", ".html"]:
            dest_folders = "Code"
        else:
            dest_folders = "Other"
            os.makedirs(os.path.join(folder, dest_folders), exist_ok=True)
            shutil.move(
                os.path.join(folder, f),
                os.path.join(folder, dest_folders, f)
)
organize("/home/mantag/test_folder")
