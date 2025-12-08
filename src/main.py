from textnode import (TextNode,
                      TextType)

from markdown import split_nodes_image, split_nodes_link

def main():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and some text",
        TextType.text,
    )

    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.text,
    )

    print(split_nodes_link([node]))
    
    node = TextNode("This is text with a `code block` word", TextType.text)
    print(split_nodes_image([node]))

if __name__ == "__main__":
    main()
