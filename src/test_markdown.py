import unittest
from markdown import (split_nodes_delimiter, 
                      extract_markdown_links,
                      extract_markdown_images,
                      split_nodes_link,
                      split_nodes_image)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold_text),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold_text),
                TextNode(" word and ", TextType.text),
                TextNode("another", TextType.bold_text),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded word", TextType.bold_text),
                TextNode(" and ", TextType.text),
                TextNode("another", TextType.bold_text),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.italic_text)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("italic", TextType.italic_text),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold_text)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.italic_text)
        self.assertListEqual(
            [
                TextNode("bold", TextType.bold_text),
                TextNode(" and ", TextType.text),
                TextNode("italic", TextType.italic_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code_text),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )
    
    def test_raise_exception(self):
        delimiter = "_"
        node = TextNode("matching closing _delimiter is not found", TextType.text)
        with self.assertRaises(Exception) as ctx:
            split_nodes_delimiter([node], delimiter, TextType.italic_text)

        self.assertEqual(str(ctx.exception), f"Invalid Markdown syntax. Matching closing {delimiter} is not found")

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertListEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
        
        text = "This is text with a link [to google.com](https://google.com)"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_links(text), [])

        text = "This is text with a link [to google.com](https://google.com)"
        self.assertEqual(extract_markdown_links(text), [("to google.com", "https://google.com")])

    def test_split_nodes_image(self):
        node = TextNode(
        "This is text with a link [to google.com](https://google.com)",
        TextType.text,
        )

        self.assertEqual(split_nodes_image([node]),
                         [TextNode("This is text with a link [to google.com](https://google.com)", TextType.text)])

        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode(
                    "second image", TextType.image, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


    def test_split_nodes_link(self):
        node = TextNode(
        "This is text with a link [to google.com](https://google.com)",
        TextType.text,
        )

        self.assertEqual(split_nodes_link([node]),
                         [TextNode("This is text with a link ", TextType.text),
                          TextNode("to google.com", TextType.link, "https://google.com")])
        
        node = TextNode(
            "This is text with a [link](https://google.com) and [another link](https://youtube.com) with text that follows",
            TextType.text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("link", TextType.link, "https://google.com"),
                TextNode(" and ", TextType.text),
                TextNode("another link", TextType.link, "https://youtube.com"),
                TextNode(" with text that follows", TextType.text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()