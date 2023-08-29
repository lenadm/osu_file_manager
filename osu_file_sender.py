import shutil
from pathlib import Path
import zipfile
import os

downloads = "C:/Users/benri/Downloads/"
maps = "E:/osu!/songs/"
skins = "E:/osu!/skins/"
extension = ('.osz', '.osk')


for file in os.listdir(downloads):
    if file.endswith(extension[0]):
        source = downloads + file
        dest = maps + file
        shutil.move(source, dest)
    elif file.endswith(extension[1]):
        source = downloads + file
        str_encode = file.encode("ascii", "ignore")
        str_decode = str_encode.decode()
        folder = Path(source).stem
        folder = ''.join(letter for letter in folder if letter.isalnum())
        rename = downloads + folder + ".zip"
        os.rename(source, rename)

        counter = 0
        with zipfile.ZipFile(rename, "r") as f:
            for name in f.namelist():
                counter = counter + 1
            if counter > 1:
                os.mkdir(downloads + folder)
                shutil.unpack_archive(rename, downloads + folder) 
                f.close()
                os.remove(rename)
            elif counter == 1:
                shutil.unpack_archive(rename, downloads + folder)
                f.close()
                os.remove(rename)
            else:
                f.close()
                os.remove(rename)
                print("empty .osk :(")

        shutil.move(downloads + folder, skins + folder)
