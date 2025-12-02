
class HTMLNode():
    def __init__(self, tag: str | None=None, value:str | None=None, 
                 children: list | None=None, props: dict| None=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        
        string = ""
        for key in self.props:
            string += f' {key}="{self.props[key]}"'
        
        return string

    def __repr__(self) -> str:
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
    