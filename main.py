from ntpath import exists
import os
import shutil

folder_path=""
 
file_type={"image":[".png",".jpg","jpeg"], "music":[".mp3",".wav",".ogg"]}

for filename in os.listdir(folder_path):
    file_path=os.path.join(folder_path,filename)
    if os.path.isfile(file_path):
        continue
    ext=os.path.splitext(filename)[1].lower()
    for folder,extensions in file_type.items():
        if ext in extensions:
            target = os.path.join(folder_path,folder)
            os.makedirs(target, exist_ok=True)
            shutil.move(file_path ,os.path.join(target ,filename))
            break
