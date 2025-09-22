from textnode import TextNode,TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from extract_title import *
import os
import sys
from shutil import copy, rmtree

def main():
  try:
    basepath = sys.argv[1]
  except Exception:
    basepath = ""
  copy_contents(f"{basepath}static", f"{basepath}docs")
  generate_pages_recursive(f"{basepath}content", "template.html", f"{basepath}docs")
  
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  source_contents = os.listdir(dir_path_content)
  print(f"These contents: {source_contents}")

  for item in source_contents:
    print(f"Analyzing: {item}")
    source_path = os.path.join(dir_path_content, item)
    dest_path = os.path.join(dest_dir_path, item)
    print(f"Source: {source_path}, Dest: {dest_path}")
    if os.path.isdir(source_path) and not os.path.isdir(dest_path):
      os.mkdir(dest_path)
      print("Recursively walking tree..")
      generate_pages_recursive(source_path, template_path, dest_path)
    elif os.path.isfile(source_path):
      print("Generating page..")
      generate_page(source_path, template_path, dest_path)
  pass


def iter_dir(source_path, dest_path, new_dir):
  new_source_path = os.path.join(source_path, new_dir)
  new_dest_path = os.path.join(dest_path, new_dir)
  print(f"New source: {new_source_path}, New dest: {new_dest_path}")

  if os.path.isfile(new_source_path):
    copy(new_source_path, new_dest_path)
  elif not os.path.exists(new_dest_path):
    os.mkdir(new_dest_path)
  else:
    next_dirs = os.listdir(new_source_path)
    for dir in next_dirs:
      iter_dir(new_source_path, new_dest_path, dir)
  return None

def copy_contents(source, dest):
  root = True
  if root:
    rmtree(dest)
    os.mkdir(dest)
    root = False
  
  source_dir = os.listdir(source)

  print(f"Starting out: {source_dir}")

  for item in source_dir:
    print(f"Working on {item}")
    source_path = os.path.join(source, item)
    dest_path = os.path.join(dest, item)
    if os.path.isdir(source_path) and not os.path.exists(dest_path):
      os.mkdir(dest_path)
    if os.path.isfile(source_path):
      copy(source_path, dest_path)
    else:
      new_dirs = os.listdir(source_path)
      for new_dir in new_dirs:
        iter_dir(source_path, dest_path, new_dir)

main()