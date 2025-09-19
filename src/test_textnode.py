import unittest

from textnode import TextNode, TextType, split_nodes_delimiter
from regexer import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_matching_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text,node2.text)
    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), result)
    def test_split_nodes_italic(self):
        node = TextNode("And here _is some more code_ input but don't format `this word`.", TextType.TEXT)
        result = [
            TextNode("And here ", TextType.TEXT),
            TextNode("is some more code", TextType.ITALIC),
            TextNode(" input but don't format `this word`.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), result)
    def test_split_nodes_bold(self):
        node = TextNode("`hopefully this` works _correctly_ or maybe **it won't**", TextType.TEXT)
        result = [
            TextNode("`hopefully this` works _correctly_ or maybe ", TextType.TEXT),
            TextNode("it won't", TextType.BOLD),
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), result)
    def test_extract_markdown_images(self):
      matches = extract_markdown_images(
          "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
      )
      self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links(self):
      matches = extract_markdown_links(
          "This is text with an [woohoo](https://i.imgur.com/zjjcJKZ.png)"
      )
      self.assertListEqual([("woohoo", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()