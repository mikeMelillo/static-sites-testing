import unittest

from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "lemmings", [], {"color": "blue"})
        node2 = HTMLNode("a", "lemmings", [], {"color": "blue"})
        self.assertEqual(node, node2)
    def test_neq_props(self):
        node = HTMLNode("a", "lemmings", [], {"color": "blue"})
        node2 = HTMLNode("a", "lemmings", [], {"color": "red"})
        self.assertNotEqual(node.props, node2.props)
    def test_eq_repr(self):
        node = HTMLNode("a", "Lemons", [], {"color": "rebeccapurple", "stroke": "black"})
        self.assertEqual(repr(node), """Tag: a, Value: Lemons, Children: [], Props: {'color': 'rebeccapurple', 'stroke': 'black'}""")
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()