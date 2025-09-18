from textnode import TextNode,TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
  tn = TextNode("Here we go!", TextType.BOLD)
  print(tn)
  hn = HTMLNode("a", "Lemons", None, {"color": "rebeccapurple", "stroke": "black"})
  print(hn)
  ln = LeafNode("a", "Home Page", {"href": "http://localhost:8889/home"})
  ln2 = LeafNode("p", "Sling", {"stroke": "blue"})
  print(ln)
  print(ln.to_html())
  pn1 = ParentNode("div", [ln2], None)
  pn = ParentNode("div", [ln,pn1], None)
  print(pn)
  print(pn.to_html())

main()