import os
import shutil
import sys
from generate_site import generate_pages_recursive
from copystatic import copy_files

def main():
    

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    content_path = "./content/"
    template_path = "./src/template.html"
    source_path = "./static/"
    target_path = "./doc/"    
   
    if os.path.exists(target_path):
        shutil.rmtree(target_path)   
            
    copy_files(source_path, target_path)
    generate_pages_recursive(base_path, content_path, template_path, target_path) 
   

if __name__ == "__main__":
    main()
