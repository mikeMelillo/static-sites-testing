from enum import Enum

class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode:
  def __init__(self, text, text_type: TextType, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url
  
  def __eq__(self, other):
    return self.text == other.text and self.text_type == other.text_type and self.url == other.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
  new_nodes = []
  for node in old_nodes:
    text = node.text
    index = text.find(delimiter)
    if index == -1 or node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    chunks = text.split(delimiter)
    if len(chunks) % 2 == 0:
      raise Exception("Unmatched delimiter present")
    for i in range(len(chunks)):
      if len(chunks[i]) == 0:
        continue
      elif i % 2 == 0:
        this_node = TextNode(chunks[i], node.text_type)
      else:
        this_node = TextNode(chunks[i], text_type)
      new_nodes.append(this_node)
  return new_nodes
