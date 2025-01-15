import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    ## PARENTNODE TESTS BELOW ##

    def test_parentnode_repr(self):
        node = ParentNode("div", [LeafNode("a", "Click me!", {"href": "https://www.google.com"})])
        self.assertEqual(repr(node), "ParentNode(div, [LeafNode(a, Click me!, {'href': 'https://www.google.com'})], None)")

    def test_parentnode_to_html(self):
        node = ParentNode("div", [LeafNode("a", "Click me!", {"href": "https://www.google.com"})])
        self.assertEqual(node.to_html(), '<div><a href="https://www.google.com">Click me!</a></div>')

    def test_parentnode_to_html_raises_value_error_if_tag_is_none(self):
        node = ParentNode(None, [LeafNode("a", "Click me!", {"href": "https://www.google.com"})])
        self.assertRaises(ValueError, node.to_html)

    def test_parentnode_to_html_raises_value_error_if_children_is_none(self):
        node = ParentNode("div", None)
        self.assertRaises(ValueError, node.to_html)

    # Test all the edge cases you can think of, including nesting ParentNode objects inside of one another, multiple children, and no children.

    def test_parentnode_to_html_can_handle_nested_parent_nodes(self):
        node = ParentNode("div", [ParentNode("span", [LeafNode("a", "Click me!", {"href": "https://www.google.com"})])])
        self.assertEqual(node.to_html(), '<div><span><a href="https://www.google.com">Click me!</a></span></div>')

    def test_parentnode_to_html_can_handle_multiple_children(self):
        node = ParentNode("div", [LeafNode("a", "Click me!", {"href": "https://www.google.com"}), LeafNode("a", "Click me!", {"href": "https://www.google.com"})])
        self.assertEqual(node.to_html(), '<div><a href="https://www.google.com">Click me!</a><a href="https://www.google.com">Click me!</a></div>')


if __name__ == "__main__":
    unittest.main()
