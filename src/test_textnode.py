import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()