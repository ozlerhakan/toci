import unittest


class MyTestCase(unittest.TestCase):

    def test_toci(self):
        from src.toci.Toci import Toci
        toci = Toci()
        toc = toci.execute('data/notebook.ipynb')

        expected_toc = """# Table of Content
- [Intro](#Intro)
  - [Heading 2](#Heading-2)
    - [Heading 3](#Heading-3)
  - [Another Heading 2](#Another-Heading-2)
  - [Another Heading 2 2](#Another-Heading-2-2)
    - [Another Heading 3](#Another-Heading-3)
      - [Another Heading 4](#Another-Heading-4)
"""
        self.assertEqual(toc, expected_toc)


if __name__ == '__main__':
    unittest.main()
