from pathlib import Path
import unittest
import os

ROOT_DIR = Path(__file__).parent


class MyTestCase(unittest.TestCase):

    def test_toci(self):
        from src.toci.Toci import Toci
        toci = Toci()
        toc = toci.execute(os.path.join(ROOT_DIR, 'data/notebook.ipynb'))

        expected_toc = """# Table of Content
- [Intro](#intro)
  - [Heading 2](#heading-2)
    - [Heading 3](#heading-3)
  - [Another Heading 2](#another-heading-2)
  - [Another Heading 2 2](#another-heading-2-2)
    - [Another Heading 3](#another-heading-3)
      - [Another Heading 4](#another-heading-4)
"""
        self.assertEqual(toc, expected_toc)


if __name__ == '__main__':
    unittest.main()
