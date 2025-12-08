from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    text = "text"
    bold_text = "bold"
    italic_text = "italic"
    code_text = "code"
    link = "link"
    image = "image"


class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node: object) -> bool:
        if not isinstance(text_node, TextNode):
            return False
        return (self.text == text_node.text and
                self.text_type == text_node.text_type and
                self.url == text_node.url)


    def __repr__(self) -> str:
        return f"TextNode({self.text}, TextType.{self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node) -> LeafNode:
    tag = None
    value = ""
    props = {}
    match text_node.text_type:
        case TextType.text:
            tag = None
            value = text_node.text
        case TextType.bold_text:
            tag = "b"
            value = text_node.text
        case TextType.italic_text:
            tag = "i"
            value = text_node.text
        case TextType.code_text:
            tag = "code"
            value = text_node.text
        case TextType.link:
            tag = "a"
            value = text_node.text
            props["href"] = text_node.url
        case TextType.image:
            tag = "img"
            props["src"] = text_node.url
            props["alt"] = text_node.text
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")

    return LeafNode(tag=tag, value=value, props=props)