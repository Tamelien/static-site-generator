def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    
    filterd_blocks = []
    
    for i in range(len(blocks)):
        if blocks[i]:
            filterd_blocks.append(blocks[i].strip())

    return filterd_blocks