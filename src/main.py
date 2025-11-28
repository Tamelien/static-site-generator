from textnode import (TextNode,
                      TextType)

def main():
    node = TextNode("hello", TextType.text)
    print(node)

if __name__ == "__main__":
    main()
