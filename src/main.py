from os import path, makedirs, listdir
from shutil import rmtree
from sys import argv

from textnode import *
from splitter import *
from htmlnode import LeafNode
from block import BlockType, block_to_block_type, markdown_to_blocks
from copystatic import copy_static_recursive

basepath = argv[1] if len(argv) > 1 else "/"

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public dir...")
    if path.exists(dir_path_public):
        rmtree(dir_path_public)
    
    print("copying static content...")
    copy_static_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    recusive_gen(dir_path_content, dir_path_public)


def recusive_gen(source_dir, public_dir):
    for item in listdir(source_dir):
        source = path.join(source_dir, item)
        dest = path.join(public_dir, item)
        print(f" * {source} -> {dest}")
        if path.isfile(source):
            if source.endswith(".md"):
                html_dest = dest.replace(".md", ".html")
            generate_page(source, html_dest, template_path)
        else:
            recusive_gen(source, dest)

def generate_page(from_path, dest_path, template_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not path.isfile(from_path):
        raise FileNotFoundError("the markdown file was not found")

    md_content = read_file(from_path)
    template = read_file(template_path)

    node = markdown_to_html_node(md_content)
    html = node.to_html()

    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    dest_dir_path = path.dirname(dest_path)
    if dest_dir_path != "":
        makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def read_file(source):
    if not path.isfile(source):
        raise FileNotFoundError("the source file not found")
    file = open(source)
    content = file.read()
    file.close()
    return content


def extract_title(md):
    if md.startswith("# "):
        return md.split("\n", 1)[0].lstrip('#').strip()
    raise Exception("No title found")

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