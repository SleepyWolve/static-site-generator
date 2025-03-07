import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node
from splitter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_none_val(self):
        node3 = TextNode("str", TextType.ITALIC, None)
        node4 = TextNode("str", TextType.ITALIC, None)
        self.assertEqual(node3, node4)
    def test_not(self):
        node5 = TextNode("str", TextType.CODE)
        node6 = TextNode("str", TextType.BOLD)
        self.assertNotEqual(node5, node6)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    # move to it's own test_file
    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                    TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT),
                                    ])
        



if __name__ == "__main__":
    unittest.main()