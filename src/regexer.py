import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
  img_text_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  return re.findall(img_text_pattern, text)

def extract_markdown_links(text):
  link_text_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  return re.findall(link_text_pattern, text)

def split_nodes_image(old_nodes:list[TextNode]):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    original_text = old_node.text
    images = extract_markdown_images(original_text)
    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    for image in images:
      sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(sections) != 2:
        raise ValueError("invalid markdown, image section not closed")
      if sections[0] != "":
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append( TextNode(image[0], TextType.IMAGE, image[1]) )
      original_text = sections[1]
    if original_text != "":
      new_nodes.append( TextNode(original_text, TextType.TEXT) )
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

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


def text_to_textnodes(text):
  initial_text_node = TextNode(text, TextType.TEXT)
  new_nodes = split_nodes_delimiter([initial_text_node], "**", TextType.BOLD)
  new_nodes = split_nodes_delimiter([new_nodes], "_", TextType.ITALIC)
  new_nodes = split_nodes_delimiter([new_nodes], "`", TextType.CODE)
  new_nodes = split_nodes_image([new_nodes])
  return split_nodes_link([new_nodes])
