from pathlib import Path
import shutil,sys

files=[]
extentions=set()

directory=input('enter target folder: ')
p=Path(directory)

if not p.is_dir():
    print('enter a folder destination')
    sys.exit(0)

def make_folders(p):
    
    for file in p.iterdir():
        if file.is_file():
            extentions.add(file.suffix.lstrip("."))

    for each in extentions:
        flag=''
        new_ext=p/each
        if new_ext==p:
           flag=p/'others'
        else:
            new_ext.mkdir()
        if not flag=='':
            flag.mkdir()
    

make_folders(p=p)
for folder in p.iterdir():
    if  folder.is_dir():
        for file in p.iterdir():
             if file.is_file():
                if folder.name==file.suffix.lstrip('.'):
                    shutil.move(file,folder)
for file in p.iterdir():
    if file.is_file():
        shutil.move(file,p/'others')

#C:\Users\Engineering CQAI\Desktop\demo_organised