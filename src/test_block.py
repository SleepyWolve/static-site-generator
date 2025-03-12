import unittest
from block import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_heading(self):
        # Test headings (1-6 # characters)
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####### Heading 7"), BlockType.HEADING)  # Too many #

    def test_code_block(self):
        # Test code blocks (multiline)
        self.assertEqual(block_to_block_type("```\code block```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```py\nprint('Hello World')\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_block_type("``inline code``"), BlockType.CODE)  # Not a code block

    def test_quote_block(self):
        # Test quote blocks
        self.assertEqual(block_to_block_type("> This is a quote."), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Another quote"), BlockType.QUOTE)
        self.assertNotEqual(block_to_block_type("Not a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        # Test unordered list items
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED)
        self.assertEqual(block_to_block_type("- Another item"), BlockType.UNORDERED)
        self.assertNotEqual(block_to_block_type("* Not a list item"), BlockType.UNORDERED)  # Wrong symbol

    def test_ordered_list(self):
        # Test ordered list items
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED)
        self.assertEqual(block_to_block_type("2. Second item"), BlockType.ORDERED)
        self.assertNotEqual(block_to_block_type("A. Not a numbered list"), BlockType.ORDERED)  # Invalid format

    def test_paragraph(self):
        # Test normal paragraphs
        self.assertEqual(block_to_block_type("This is a normal paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Another paragraph with no special formatting."), BlockType.PARAGRAPH)
        self.assertNotEqual(block_to_block_type("# Not a paragraph"), BlockType.PARAGRAPH)  # It's a heading

    def test_empty_block(self):
        # Test empty or whitespace-only blocks
        self.assertIsNone(block_to_block_type(""))  # Empty string
        self.assertIsNone(block_to_block_type("   "))  # Whitespace only
        self.assertIsNone(block_to_block_type("\n\n"))  # Newlines only
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()