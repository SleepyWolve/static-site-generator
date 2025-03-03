import unittest

from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_all(self):
        node = HTMLNode("a", "text inside the tag", None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = node.props_to_html()
        node3 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node2, node3)
        node4 = HTMLNode("p", "str", node, {"href": "link" })
        node5 = HTMLNode()
        self.assertNotEqual(node4, node5)
        node6 = HTMLNode("p", "paragraph", node4, {"href": "boot.dev" })
        node7 = HTMLNode("p", "paragraph", node4, {"href": "boot.dev" })
        self.assertEqual(node6, node7)
        self.assertEqual(node.__repr__(), "HTMLNode(a, text inside the tag, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")


if __name__ == "__main__":
    unittest.main()