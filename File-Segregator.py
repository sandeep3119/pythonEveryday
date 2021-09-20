import os
import shutil 

print(os.getcwd())

data = os.listdir(".")

for file_ in  data:
    # print(file_)
    dir_name=file_.split(".")[-1]
    os.makedirs(dir_name,exist_ok=True)
    if (os.path.isfile(file_) and file_!='script.py') :
        src_file_path=file_
        dest_file_path=os.path.join(dir_name,file_)
        shutil.move(src_file_path,dest_file_path)



