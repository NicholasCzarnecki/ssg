from textnode import TextNode
from textnode import TextType


def main():
    node = TextNode("Test", TextType.NORMAL, "www.google.com")
    print(node.__repr__())


main()
