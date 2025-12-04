from textnode import (TextNode,
                      TextType)

from htmlnode import (LeafNode)

def main():
    node = LeafNode("p", "Hello, world!")
    print(node)

if __name__ == "__main__":
    main()
