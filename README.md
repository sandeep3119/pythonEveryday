# pythonEveryday
Small scripts to automate day to day tasks using python


### flask-template-create.py
Create a basic project structure for flask project.
```bash
python flask-template-create.py --app-name=YOUR_APP_NAME
```
* By default --app-name=ROOT

### image-scaling.py
Create a folder with all scaled images used to train Neural Networks.
```bash
python image-scaling.py --folder_path=YOUR_FOLDER_PATH --w= WIDTH --h= Height
```
* By default --folder_path=Current working directory --w=400 --h=400

### File-Segregator.py
Segregates files based upon extensions and move to different folders.
```bash
python FileSegregator.py --target=YOUR_TARGET_FOLDER
```
* By default --target=Current working directory

### Weeding-Script.py
Moves all non-image/corrupt files to the specified Trash Folder.
```bash
python Weeding-Script.py --target=YOUR_TARGET_FOLDER
```
* By default --target=Current working directory




