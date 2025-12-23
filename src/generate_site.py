import os
from copystatic import copy_files
from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown: str) -> str:
   
    for line in markdown.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    raise Exception("no header found")

def generate_page(base_path: str, source_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {source_path} to {dest_path} using {template_path}")

    with open(source_path) as file:
        content = file.read()
        
    title = extract_title(content)

    html = markdown_to_html_node(content).to_html()

    with open(template_path) as file:
        template = file.read()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    if base_path == "/":
        base_path = "/"
    else:
        base_path = base_path.lstrip("/")
        base_path = base_path.rstrip("/")
        base_path = "/" + base_path + "/"
    
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')

    dest_dir = os.path.dirname(dest_path)

    if not os.path.exists(dest_dir) and dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(template)

def generate_pages_recursive(base_path: str, content_dir_path: str, template_path: str, dest_dir_path: str):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for path in os.listdir(content_dir_path):
        content_path = os.path.join(content_dir_path, path)
        dest_path = os.path.join(dest_dir_path, path)

        if os.path.isdir(content_path):
            generate_pages_recursive(base_path, content_path, template_path, dest_path)
        else:
            if content_path.endswith(".md"):
                filename, _ = os.path.splitext(dest_path)
                generate_page(base_path, content_path, template_path, filename + ".html")