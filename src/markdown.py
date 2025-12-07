from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
  
    
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) == 1:
            new_nodes.append(node)
            continue

        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax. Matching closing {delimiter} is not found")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(part, TextType.text))
            else:
                if part:
                    new_nodes.append(TextNode(part, text_type))


    return new_nodes