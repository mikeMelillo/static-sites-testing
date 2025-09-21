from textnode import TextNode,TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
from shutil import copy, rmtree

def main():
  copy_contents("static", "public")

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

def copy_contents(source:str="static", dest:str="public"):
  root = True
  if root:
    rmtree(dest)
    os.mkdir(dest)
    root = False
  
  #iter_dir(source, dest, current_path = None)
  source_dir = os.listdir(source)
  print(f"Source Dir: {source_dir}")

  for item in source_dir:
    source_path = os.path.join(source, item)
    dest_path = os.path.join(dest, item)
    print(f"Source path: {source_path}, Dest path: {dest_path}")
    if not os.path.exists(dest_path):
      print("Making dir")
      os.mkdir(dest_path)
    if os.path.isfile(source_path):
      print("Copying file")
      copy(source_path, dest_path)
    else:
      print(f"Iterating for {dest_path}")
      new_dirs = os.listdir(source_path)
      print(f"New Dirs: {new_dirs}")
      for new_dir in new_dirs:
        iter_dir(source_path, dest_path, new_dir)      

  print(source_dir)

main()