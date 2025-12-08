from textnode import (TextNode,
                      TextType)

from markdown import extract_markdown_images, extract_markdown_links

def main():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    print(extract_markdown_links(text))
    text = "This is text with a link [to google.com](https://google.com) and [to youtube](https://www.youtube.com)"
    print(extract_markdown_images(text))
    print(extract_markdown_links(text))

if __name__ == "__main__":
    main()
