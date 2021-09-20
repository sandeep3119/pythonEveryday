import os
import shutil
from PIL import Image
import argparse


def main(TARGET_DIR):
    os.chdir(TARGET_DIR)
    os.makedirs("Trash",exist_ok=True)
    files=os.listdir(".")
    for file_ in files:
        try:
            Image.open(file_)
        except Exception as e:
            shutil.move(file_,os.path.join("Trash",file_))


if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--target",default=os.getcwd())
    parsed_args=args.parse_args()
    main(TARGET_DIR=parsed_args.target)