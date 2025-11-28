import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold_text)
        node2 = TextNode("This is a text node", TextType.bold_text)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node1 = TextNode("Test", TextType.image)
        self.assertEqual(node1.url, None)
        node2 = TextNode("Test", TextType.link, "Url")
        self.assertEqual(node2.url, "Url")
    
    def test_print(self):
        for type in TextType:
            node = TextNode("Test", type)
            print(node)
            self.assertEqual(node.text_type.value, type.value)

if __name__ == "__main__":
    unittest.main()
