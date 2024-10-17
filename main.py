import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.join(downloads_folder, "images")
extensions = [".jpg", ".jpeg", ".avif", ".png", ".tiff"]

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

for filename in os.listdir(downloads_folder):
    file_ext = os.path.splitext(filename)[1].lower()
   
    if file_ext in extensions :
        print(f"Moving {filename} to images folder")
        file_path = os.path.join(downloads_folder, filename)
        shutil.move(file_path, images_folder)
        
    else:
        print(f"Skipping {filename}")
print("Images moved successfully")