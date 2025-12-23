from enum import Enum
import re


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    
    filterd_blocks = []
    
    for i in range(len(blocks)):
        if blocks[i]:
            filterd_blocks.append(blocks[i].strip())

    return filterd_blocks

def block_to_block_type(markdown: str) -> BlockType:
    
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.code   
        
    lines = markdown.split("\n")

    if len(lines) == 1 and re.match(r"#{1,6} ", markdown):
        return BlockType.heading

    if all(re.match(r"^>", line) for line in lines):
        return BlockType.quote

    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.unordered_list

    if all(re.match(r"^\d+\. ", line) for line in lines):
        for i, line in enumerate(lines, start=1):
            m = re.match(r"^(\d+)\. ", line)
            if int(m.group(1)) != i: # type: ignore 
                return BlockType.paragraph
        return BlockType.ordered_list  

    return BlockType.paragraph


