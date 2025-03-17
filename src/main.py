from textnode import *
from splitter import *
from htmlnode import LeafNode
from block import BlockType, block_to_block_type, markdown_to_blocks


def main():
    pass


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
        case _:
            raise Exception

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def list_to_html_node(lst, i):
    items = lst.split("\n")
    html_items = []
    for item in items:
        text = item[i:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return html_items

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            line = block.split("\n")
            paragraph = " ".join(line)
            return ParentNode("p", text_to_children(paragraph))
        case BlockType.HEADING:
            level = block[0:7].count("#")
            return ParentNode(f"h{level}", text_to_children(block[level + 1:]))
        case BlockType.CODE:
            text_node = TextNode(block[4:-3], TextType.TEXT)
            child = text_node_to_html_node(text_node)
            code = ParentNode("code", [child])
            return ParentNode("pre", [code])
        case BlockType.ORDERED:
            return ParentNode("ol", list_to_html_node(block, 3))
        case BlockType.UNORDERED:
            return ParentNode("ul", list_to_html_node(block, 2))
        case BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line.lstrip(">").strip())
            return ParentNode("blockquote", text_to_children(" ".join(new_lines)))
        
        case _:
            raise ValueError("invalid block type")


if __name__ == "__main__":
    main()