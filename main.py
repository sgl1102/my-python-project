import os
import shutil

# CHANGE THIS PATH to the folder you want to organize
Target_Folder =r"D:\Downloads"

# TYPES of files you want to organize
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".doc", ".pdf", ".pptx", ".docx", ".xlcs"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Music": [".mp3"],
    "Programs": [".exe"],
}

def sort_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
    
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                destination_folder = os.path.join(folder_path, folder_name)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break

        # Files with unknown extensions
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

    print("File sorting completed!")

if __name__ == "__main__":
    sort_files(Target_Folder)


