from textnode import (TextNode,
                      TextType)

from markdown_blocks import markdown_to_blocks, block_to_block_type

def main():
    md = """
# Heading 1

##Heading 2

### Heading 3

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

1. Item 1
2. Item 2
3. Item 3

```
This is code
```

> This is a quote.
> This is a quote.
> This is a quote.

> This is a quote.
This is a quote.
> This is a quote.

1. First item
3. Third item
2. Second item

- This is an unordered list item
1. This looks like an ordered list

"""
    blocks = markdown_to_blocks(md)
    print(blocks)

    for block in blocks:
        print(block_to_block_type(block))

    

if __name__ == "__main__":
    main()
