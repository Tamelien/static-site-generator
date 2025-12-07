from textnode import (TextNode,
                      TextType)

from markdown import split_nodes_delimiter

from htmlnode import (LeafNode)

def main():
    node1 = TextNode("This is text with a `code block` word", TextType.text)
    node2 = TextNode("This is an _italic_ word.", TextType.italic_text)
    node1 = TextNode("code block word", TextType.text)
    new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.code_text)

    print(new_nodes)

if __name__ == "__main__":
    main()
