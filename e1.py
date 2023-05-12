import glob

print(glob.glob("*.txt"))
txtfiles=glob.glob("*.txt")
for filepath in txtfiles:
    with open(filepath) as file:
        print(file.read())
        