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
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_link(self):
        node = LeafNode("p", "Hello, world!", {"href": "boot.dev" })
        self.assertEqual(node.to_html(), '<p href="boot.dev">Hello, world!</p>')
    def test_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()