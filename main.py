from pathlib import Path
import shutil

files=[]
extentions=[]

directory=input('enter target folder: ')
p=Path(directory)

if not p.is_dir():
    print('enter a folder destination')

for file in p.iterdir():
    if file.is_file():
        files.append(file)

for mango in files:
    extentions.append(mango.suffix.lstrip('.'))

unique_extentions=set(extentions)

created_foulders=[]

for unique in unique_extentions:
    new_ext=p / unique      
    if not new_ext.exists():
        new_ext.mkdir()
        created_foulders.append(new_ext)
        print(f'{new_ext} foulder created')
    else:
        print(f'{new_ext} folder already exists')

print(f'created_foulders={created_foulders}')


for folder in p.iterdir():
    if  folder.is_dir():
        for file in p.iterdir():
             if file.is_file():
                  shutil.move(file,folder)

#C:\Users\Engineering CQAI\Desktop\demo_organised