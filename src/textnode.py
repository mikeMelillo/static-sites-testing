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

def lookup_md_delimiter(text_type:TextType)->str:
  if text_type == TextType.TEXT:
    return ""
  elif text_type == TextType.BOLD:
    return "**"
  elif text_type == TextType.ITALIC:
    return "_"
  elif text_type == TextType.CODE:
    return "`"
  elif text_type == TextType.LINK:
    return "["
  elif text_type == TextType.IMAGE:
    return "!["

def md_delimiter_order()->list:
  return [
    TextType.CODE,
    TextType.BOLD,
    TextType.ITALIC,
    TextType.IMAGE,
    TextType.LINK,
    TextType.TEXT
  ]

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
  pass