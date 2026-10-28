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
    extentions.append(mango.suffix.lstrip('.'))

unique_extentions=set(extentions)

print(unique_extentions)

for unique in unique_extentions:
    new_ext=p / unique
    if not new_ext.exists():
        new_ext.mkdir()
        print(f'{new_ext} foulder created')
    else:
        print(f'{new_ext} folder already exists')