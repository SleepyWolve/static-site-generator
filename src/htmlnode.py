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
