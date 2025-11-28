from enum import Enum

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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"