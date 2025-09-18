import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_has_link(self):
        node = LeafNode("a", "Home", {"href": "/home"})
        self.assertEqual(node.to_html(), '<a href="/home">Home</a>')

if __name__ == "__main__":
    unittest.main()