from textnode import (TextNode,
                      TextType)

from markdown import text_to_textnodes

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a [link](https://youtube.com) with extra text"

    print(text_to_textnodes(text))
    

if __name__ == "__main__":
    main()
