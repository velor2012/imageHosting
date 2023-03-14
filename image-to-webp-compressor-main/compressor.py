import os
from PIL import Image
from pathlib import Path

def all_files(directory):
    for path, dirs, files in os.walk(directory): # walks through the folder
        for f in files:
            yield os.path.join(path, f)


files = [f for f in all_files('E:\\新建文件夹\\OneDrive - 同济大学\\github_repos\\blog\\23.nat服务器使用cf tunnel建站') # Edit your name
               if f.endswith(('.png', '.jpg', 'jpeg'))]

def convert_to_webp(source):
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp
    return image


for file in files:
    path = Path(file)
    convert_to_webp(path)
    # os.remove(path) # removes previous images after conversion