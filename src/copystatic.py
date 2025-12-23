import os
import shutil


def copy_files(source_dir_path: str, target_dir_path: str):
    if not os.path.exists(target_dir_path):
        print(f" make dir {target_dir_path}")
        os.mkdir(target_dir_path)

    for path in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, path)
        target_path = os.path.join(target_dir_path, path)
        
        if os.path.isdir(source_path):
            copy_files(source_path, target_path)
        else:
            print(f" copy {source_path} -> {target_path}")
            shutil.copy(source_path, target_path)