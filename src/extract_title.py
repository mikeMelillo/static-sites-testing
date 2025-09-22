import os
from block_conversion import markdown_to_html_node

def extract_title(markdown):
  lines = markdown.splitlines()
  header_line = None
  for line in lines:
    if line.startswith("# "):
      header_line = line
  if header_line == None:
    raise Exception("No header linke (#) found")
  return header_line.lstrip("# ")

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page {from_path}, to {dest_path}, using {template_path}")
  if not os.path.isfile(from_path):
    raise Exception("Input file 'from_path' is not a file")
  if not os.path.isfile(template_path):
    raise Exception("Template file 'template_path' is not a file")
  with open(from_path, 'r') as file:
    markdown = file.read()
  with open(template_path) as file:
    html_input = file.read()
  
  html_nodes = markdown_to_html_node(markdown).to_html()
  title = extract_title(markdown)
  html_input = html_input.replace("{{ Title }}", title)
  html_input = html_input.replace("{{ Content }}", html_nodes)
  dest_dirs = dest_path.split("/")
  full_dir = ""

  for dir in dest_dirs:
    if dir.endswith(".html") or dir.endswith(".md"):
      continue
    full_dir = os.path.join(full_dir, dir)
    if not os.path.exists(full_dir):
      os.mkdir(full_dir)
      pass

  if dest_path.endswith(".md"):
    dest_path = dest_path.replace(".md", ".html")
  with open(dest_path, "w") as file:
    file.write(html_input)
