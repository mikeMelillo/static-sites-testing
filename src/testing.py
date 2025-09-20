from block_conversion import markdown_to_html_node
from htmlnode import HTMLNode

md = """
# My big header

## A subheader

This is **bolded** paragraph

## Another Subheader

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

### A real tiny subheader

- This is a list
- with items
"""

results = markdown_to_html_node(md)

print(f"Html nodes: {results}")
print(f"Resulting html: {results.to_html()}")