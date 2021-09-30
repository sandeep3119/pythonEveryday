import os
from PIL import Image
import argparse
import shutil


def main(folderPath, height, width):
    if(folderPath != os.getcwd()):
        os.chdir(folderPath)
    os.makedirs('scaled_images', exist_ok=True)
    data = os.listdir('.')
    count = 0
    for _file in data:
        try:
            image = Image.open(_file)
            if(image.width < width or image.height < height):
                print(f'Skipping file - {_file}  as width or height less than target parameters')
                continue
    
            image = image.resize((width, height))
            file_name=f'resized_{count}.jpg'
            image.save(file_name)
            shutil.move(file_name, os.path.join(
                    'scaled_images', file_name))
            count += 1

        except Exception as e:
            pass


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--folder-path', default=os.getcwd())
    args.add_argument('--h', default=400)
    args.add_argument('--w', default=400)
    parsed_args = args.parse_args()
    main(parsed_args.folder_path, parsed_args.w, parsed_args.h)
