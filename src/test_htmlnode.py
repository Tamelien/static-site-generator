import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()