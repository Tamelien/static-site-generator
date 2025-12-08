from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue
        
        text = node.text

        for image_alt, image_link in images:
            parts = text.split(f"![{image_alt}]({image_link})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.text))
            
            new_nodes.append(TextNode(image_alt, TextType.image, image_link))

            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.text))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        
        if not links:
            new_nodes.append(node)
            continue
        
        text = node.text

        for alt, link in links:
            parts = text.split(f"[{alt}]({link})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.text))
            
            new_nodes.append(TextNode(alt, TextType.link, link))

            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.text))

    return new_nodes
