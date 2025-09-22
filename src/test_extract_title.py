import unittest

from extract_title import extract_title

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        markdown_input = """
# Ring ring, bananaphone
## Banana phooooone
```
Crazy codeblock stuff
```
"""
        output = "# Ring ring, bananaphone"
        self.assertEqual(output, extract_title(markdown_input))
if __name__ == "__main__":
    unittest.main()