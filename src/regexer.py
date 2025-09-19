import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
  img_text_pattern = r"!\[(.*?)\]\((.*?)\)"
  return re.findall(img_text_pattern, text)

def extract_markdown_links(text):
  link_text_pattern = r"\[(.*?)\]\((.*?)\)"
  return re.findall(link_text_pattern, text)

def split_nodes_image(old_nodes):
  pass

def split_nodes_link(old_nodes):
  pass