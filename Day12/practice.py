# Write a script that reads all files in a folder, gets each file's modified date using Path.
# stat(), and moves files into subfolders named by year (e.g. output/2024/). Combine pathlib + datetime.

from pathlib import Path
from datetime import datetime
import os
import shutil

p = Path(r"C:\Users\vhari\Desktop\AI_ENGINEER")

for file in p.iterdir():
    if file.is_file():
        sfile=file.stat()
        filesize = sfile.st_size
        modified_date = datetime.fromtimestamp(sfile.st_mtime)
        print(f"{file}={filesize} + {modified_date.year}")
        
        y = modified_date.year

        d_folder = p/str(y)
        d_folder.mkdir(exist_ok=True)

        # file.rename(d_folder/file.name)
        #shutil.copy(file, d_folder)





