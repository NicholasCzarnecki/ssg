from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode, LeafNode


def main():
    node = LeafNode("p", "This is a paragraph of text.")

    print(node.to_html())
    print(repr(node))

main()
