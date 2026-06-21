import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Desktop") # Can write whatever directory you want to organize.

extensions = {
     ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mp3": "Music",
    ".py": "PythonProjects",
    ".doc": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
 }

for filename in os.listdir(directory):
     file_path = os.path.join(directory, filename)

     if os.path.isfile(file_path):
         extension = os.path.splitext(filename)[1].lower()

         if extension in extensions:
             folder_name = extensions[extension]

             folder_path = os.path.join(directory, folder_name)
             os.makedirs(folder_path, exist = True)

             destination_path = os.path.join(folder_path, filename)
             shutil.move(file_path, destination_path)

             print(f"Moved {filename} to {folder_name} folder.")
         else:
             print(f"Skipped {filename}. Unkown file extension.")
     else:
         print(f"Skipped {filename}. It is a directory.")

print("File organization complete.")

