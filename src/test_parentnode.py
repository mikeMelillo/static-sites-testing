import unittest

from htmlnode import ParentNode, LeafNode


def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_html_grandchildren_2(self):
    ln = LeafNode("a", "Home Page", {"href": "http://localhost:8889/home"})
    ln2 = LeafNode("p", "Sling", {"stroke": "blue"})
    pn1 = ParentNode("div", [ln2], None)
    pn = ParentNode("div", [ln,pn1], None)
    output = """<div><a href="http://localhost:8889/home">Home Page</a><div><p stroke="blue">Sling</p></div></div>"""
    self.assertEqual(pn.to_html(), output)

if __name__ == "__main__":
    unittest.main()