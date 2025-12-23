import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_heading(self):
        md = """
### This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a heading</h3></div>",
        )


    def test_quote(self):
        md = """
> This is a quote
>
> spanning multiple lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote  spanning multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item
- Second item
- Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>",
        )


    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_multiline_heading_is_paragraph(self):
        md = """
# Heading one
## Heading two
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p># Heading one ## Heading two</p></div>",
        )

    def test_invalid_quote_is_paragraph(self):
        md = """
> This is a quote
This is not
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>> This is a quote This is not</p></div>",
        )

    def test_invalid_ordered_list_is_paragraph(self):
        md = """
1. First item
3. Second item
4. Third item
5. Fourth item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>1. First item 3. Second item 4. Third item 5. Fourth item</p></div>",
        )

    def test_empty_markdown(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")
    
    def test_quote_with_inline(self):
        md = """
> This is a _fancy_ **quote**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <i>fancy</i> <b>quote</b></blockquote></div>",
        )


    def test_mixed_blocks(self):
        md = """
# Title

Paragraph with `code`.

- Item 1
- Item 2
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title</h1><p>Paragraph with <code>code</code>.</p><ul><li>Item 1</li><li>Item 2</li></ul></div>",
        )

if __name__ == "__main__":
    unittest.main()