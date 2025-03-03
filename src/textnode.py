from enum import Enum

class TextType(Enum):
    NORMAL = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code block"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    """docstring for TextNode."""
    def __init__(self, text, text_type, url):
        super(TextNode, self).__init__()
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False

# Note: you may want to use .value on the text_type field to get the string representation of the enum.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        


