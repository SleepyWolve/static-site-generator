from textnode import *

#needs to print "TextNode(This is some anchor text, link, https://www.boot.dev)" using TextNode
def main():
    textnode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(textnode)


if __name__ == "__main__":
    main()