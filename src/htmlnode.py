class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # HTML tag name
        self.value = value          # Value of HTML tag  
        self.children = children    # List of HTMLNode objects
        self.props = props          # Dict of key-value pairs

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        lst = []
        if self.props is None:
            return ""
        for key in self.props:
            lst.append(f'{key}="{self.props[key]}"')
        return f" {' '.join(lst)}"
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == self.props:
            return True
        else:
            return False


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=[], props=props)
        if value is None:
            raise ValueError("LeafNode must have a value")
     
    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=[], children=children, props=props)
        if tag is None:
            raise ValueError("Parent is missing a tag")
        if children  is None:
            raise ValueError("Parent needs children")
        
    def to_html(self):
        result = ""
        for child in self.children:
            result += child.to_html()
        
        return f"<{self.tag}>{result}</{self.tag}>"
