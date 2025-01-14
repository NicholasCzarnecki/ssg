import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
