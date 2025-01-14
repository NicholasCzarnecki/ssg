import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("div", "This is a test node", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        self.assertEqual(
            repr(node), "HTMLNode(div, This is a test node, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("div", "This is a test node", None, props)
        node.props_to_html()
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')
        
    def test_no_props_returns_empty_string(self):
        node = HTMLNode("div", "This is a test node", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode("div", "This is a test node", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertRaises(NotImplementedError, node.to_html)

    ## LEAFNODE TESTS BELOW ##

    def test_leafnode_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(repr(node), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")

    def test_leafnode_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_to_html_raises_value_error(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertRaises(ValueError, node.to_html)
    
    def test_leafnode_to_html_returns_value_if_tag_is_none(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Click me!")


if __name__ == "__main__":
    unittest.main()
