from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING ="heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

# regex <3
regex_patterns = {
BlockType.HEADING: re.compile(r'^(#{1,6}\s.*)$'),
BlockType.CODE: re.compile(r'^```[\s\S]*?```$'),
BlockType.QUOTE: re.compile(r'^(>\s[^\n]*(?:\n>\s[^\n]*)*)$'),
BlockType.UNORDERED: re.compile(r'^(-\s[^\n]*(?:\n-\s[^\n]*)*)$'),
BlockType.ORDERED: re.compile(r'^(\d+\.\s[^\n]*(?:\n\d+\.\s[^\n]*)*)$'),
BlockType.PARAGRAPH: re.compile(r'^(\S.+)$'),
}

def block_to_block_type(block):
    for block_type, pattern in regex_patterns.items():
        if pattern.match(block):
            return block_type
    return None

    

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    result = []
    for block in blocks:
        if block == "":
            continue
        result.append(block.strip())
    return result

