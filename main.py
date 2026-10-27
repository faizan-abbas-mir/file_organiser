from pathlib import Path
directory=input('enter target folder: ')



p=Path(directory)

if not p.is_dir:
    print('enter a folder destination')



files=[]
extentions=[]

for file in p.iterdir():
    if file.is_file():
        files.append(file)

for mango in files:
    extentions.append(mango.suffix)

print(extentions)