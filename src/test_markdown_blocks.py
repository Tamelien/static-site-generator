import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        md = """
# Heading 1

## Heading 2

## Heading 3
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.heading)

        md = """
# Heading 1
## Heading 2
## Heading 3
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.paragraph)


    def test_block_to_block_type_code(self):
        md = """
```
This is code with a list
1. Item 1
2. Item 2
3. Item 3 
```
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.code)



    def test_block_to_block_type_quote(self):
        md = """
> This is a quote.
>
> This is a quote.
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.quote)
        
        md = """
> This is a quote.
This is a quote.
> This is a quote.
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.paragraph)


    def test_block_to_block_type_ordered_list(self):
        md = """
1. First item
3. Third item
2. Second item
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.paragraph)

        md = """
1. First item
2. Third item
3. Second item
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_block_to_block_type_unordered_list(self):
        md = """
- First item
- Third item
- Second item
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.unordered_list)


        md = """
- This is an unordered list item
1. This looks like an ordered list
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            self.assertEqual(block_to_block_type(block), BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()