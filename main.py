from pathlib import Path
directory=input('enter target folder:\n')

p=Path(directory)

print(p.name)

files=[]

for file in p.iterdir():
    files.append(file)
print(files)