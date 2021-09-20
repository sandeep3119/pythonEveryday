import os
import shutil 
import argparse


def main(TARGET_DIR):
    os.chdir(TARGET_DIR)
    data = os.listdir(".")
    for file_ in  data:
        dir_name=file_.split(".")[-1]
        os.makedirs(dir_name,exist_ok=True)
        if (os.path.isfile(file_) and file_!='script.py') :
            src_file_path=file_
            dest_file_path=os.path.join(dir_name,file_)
            shutil.move(src_file_path,dest_file_path)

if __name__=='__main__':
    args=argparse.ArgumentParser()
    parsed_args=args.parse_args('--target',default=os.getcwd())
    main(parsed_args.target)

