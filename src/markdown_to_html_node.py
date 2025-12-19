from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from markdown_blocks import BlockType
import re

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        leaf_nodes = []
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.paragraph:
                lines = block.split("\n")
                text = " ".join(lines)
                text_nodes = text_to_textnodes(text)
                leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                block_nodes.append(ParentNode("p", leaf_nodes))
            case BlockType.heading:
                match = re.match(r"(#{1,6}) (.+)",block)
                if match is None:
                    raise ValueError("Invalid heading block")
                level = len(match.group(1))
                text = match.group(2)               
                text_nodes = text_to_textnodes(text)
                leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                block_nodes.append(ParentNode(f"h{level}", leaf_nodes))
            case BlockType.code:
                lines = block.split("\n")
                code_text = "\n".join(lines[1:-1]) + "\n"
                node = ParentNode("pre",
                                  [ParentNode("code", [LeafNode(None, code_text)])]
                                  )
                block_nodes.append(node)
            case BlockType.quote:
                lines = block.split("\n")
                cleaned = [line.lstrip(">").strip() for line in lines]
                text_nodes = text_to_textnodes(" ".join(cleaned))
                leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                block_nodes.append(ParentNode("blockquote", leaf_nodes))
            case BlockType.unordered_list:
                lines = block.split("\n")
                items = [line[2:] for line in lines]
                list_nodes = []

                for item in items:
                    text_nodes = text_to_textnodes(item)
                    leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                    list_nodes.append(ParentNode("li", leaf_nodes))

                block_nodes.append(ParentNode("ul", list_nodes))

            case BlockType.ordered_list:
                lines = block.split("\n")
                items = [re.sub(r"^\d+\. ", "", line) for line in lines]
                list_nodes = []

                for item in items:
                    text_nodes = text_to_textnodes(item)
                    leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                    list_nodes.append(ParentNode("li", leaf_nodes))

                block_nodes.append(ParentNode("ol", list_nodes))

            case _:
                raise ValueError(f"invalid block type: {block_type}")        

    return ParentNode("div", block_nodes)

   