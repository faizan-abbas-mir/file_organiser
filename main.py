from pathlib import Path


files=[]
extentions=[]

directory=input('enter target folder: ')
p=Path(directory)

if not p.is_dir:
    print('enter a folder destination')

for file in p.iterdir():
    if file.is_file():
        files.append(file)

for mango in files:
    extentions.append(mango.suffix)

print(extentions)