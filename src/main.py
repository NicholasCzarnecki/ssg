from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode


def main():
    node = TextNode("Test", TextType.NORMAL, "www.google.com")
    print(node.__repr__())

    node2 = HTMLNode("div", "This is a text node", None, {
        "href": "https//www.google.com",
        "target": "_blank",
    })

    print(node2.__repr__())
    print(node2.props_to_html())


main()
