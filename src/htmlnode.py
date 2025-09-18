from textnode import TextNode, TextType

class HTMLNode:
  def __init__(self, tag=None, value=None, children:list=None, props:dict=None):
    self.tag = tag
    self.value = value
    self.children = children or []
    self.props = props or {}
  
  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    res = ""
    for key,value in self.props:
      res += f' {key}="{value}"'
    return res
  
  def __eq__(self, other):
    return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

  def __repr__(self) -> str:
    return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props:dict=None):
    super().__init__(tag, value, [], props)
  
  def to_html(self):
    if self.value == None:
      raise ValueError("Node has no value set")
    if self.tag == None:
      return str(self.value)
    props_str = f''
    if self.props != None:
      for key,value in self.props.items():
        props_str += f' {key}="{value}"'
    output = f'<{self.tag}{props_str}>{str(self.value)}</{self.tag}>'
    return output
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props:dict=None):
    super().__init__(tag, None, children=children, props=props)
  
  def to_html(self):
    if self.tag == None:
      raise ValueError("No tag set")
    if self.children == None or len(self.children) == 0:
      raise ValueError("No children defined for parent node")
    props_str = f''
    children_str = f''
    for child in self.children:
      children_str += child.to_html()
    if self.props != None:
      for key,value in self.props.items():
        props_str += f' {key}="{value}"'
    output = f'<{self.tag}{props_str}>{children_str}</{self.tag}>'
    return output
    
def text_node_to_html_node(text_node:TextNode):
  if text_node.text_type == TextType.TEXT:
    return LeafNode(value=text_node.text)
  elif text_node.text_type == TextType.BOLD:
    return LeafNode("b", text_node.text)
  elif text_node.text_type == TextType.ITALIC:
    return LeafNode("i", text_node.text)
  elif text_node.text_type == TextType.CODE:
    return LeafNode("code", text_node.text)
  elif text_node.text_type == TextType.LINK:
    return LeafNode("a", text_node.text, {"href": text_node.url})
  elif text_node.text_type == TextType.IMAGE:
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
  else:
    return ValueError("No valid text type for html conversion found")