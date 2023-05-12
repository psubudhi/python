import pathlib
import zipfile

def make_archive(filepaths,dest_folder) :
    dest_path=pathlib.Path(dest_folder,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for files in filepaths:
            archive.write(files)

if __name__ == "__main__" :
    make_archive(filepaths=["a.txt","b.txt"],dest_folder="dest")
