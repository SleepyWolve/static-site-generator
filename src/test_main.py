import unittest

from main import extract_title

class extraction(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Is title\nnewline"), "Is title")
    def test_exeption_title(self):
        inputs = [
            "",
            "## Not a title",
            "No title here",
            " # Leading space",
            ]
        for input in inputs:
            with self.subTest(input=input):
                with self.assertRaises(Exception) as context:
                    extract_title(input)
                self.assertEqual(str(context.exception), "No title found")
