from main import text_node_to_html_node
from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            if not delimiter in node.text:
                raise Exception("Missing Delimiter")
            node_text = node.text.split(delimiter)
            nodes = [TextNode(node_text[0], TextType.TEXT), TextNode(node_text[1], text_type), TextNode(node_text[2], TextType.TEXT)]
            new_nodes.extend(nodes)
            continue
        new_nodes.append(node)
    return new_nodes
'''

# images
r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_images(text):
    pass