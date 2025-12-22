import shutil
import os
from copystatic import copy_files

def main():

    target_path = "./public/"    
    source_path = "./static/"

    if os.path.exists(target_path):
        shutil.rmtree(target_path)   
            
    copy_files(source_path, target_path)

if __name__ == "__main__":
    main()
