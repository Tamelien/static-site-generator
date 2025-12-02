import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com",
               "target": "_blank",}
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=props)
                        
        self.assertEqual(node.props_to_html(), expected)

        node_empty = HTMLNode(props={})
        self.assertEqual(node_empty.props_to_html(), "")

        node_none = HTMLNode()
        self.assertEqual(node_none.props_to_html(), "")
    

    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(props=props)

        expected = (
            "Tag: None, Value: None, Children: None, "
            "Props: {'href': 'https://www.google.com', 'target': '_blank'}"
        )

        self.assertEqual(repr(node), expected)

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_text(self):
        node = LeafNode(None, "Test leaf node only text")
        self.assertEqual(node.to_html(), "Test leaf node only text")

    def test_leaf_to_html_value_error(self):
        node = LeafNode(None, None) # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()