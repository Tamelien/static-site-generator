from textnode import (TextNode,
                      TextType)

from markdown_blocks import markdown_to_blocks

def main():
    markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item"""

    print(markdown_to_blocks(markdown))
    

if __name__ == "__main__":
    main()
