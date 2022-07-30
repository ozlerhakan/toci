import argparse
import nbformat
import mistune
import sys

from traitlets.config import Config
from nbconvert import NotebookExporter
from nbconvert.preprocessors import Preprocessor


class HighlightRenderer(mistune.Renderer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.toc_count = 0
        self.headers = []

    def header(self, text, level, raw=None):
        """Rendering header/heading tags like ``<h1>`` ``<h2>``.

        :param text: rendered text content for the header.
        :param level: a number for the header level, for example: 1.
        :param raw: raw text content of the header.
        """
        self.headers.append((text, level, self.toc_count))
        self.toc_count += 1
        return '<h%d>%s</h%d>\n' % (level, text, level)

    def render_toc(self):
        """Rendering headers to generate toc.

        :return: generated toc from headers.
        """
        content = '# Table of Content'
        content += '\n'
        for toc in self.headers:
            text, level, count = toc
            content += ('' if level == 1 else '  ' * (level - 1)) + '- ' + self._link(text, text)
            content += '\n'
        return content

    def _link(self, link, text):
        """Rendering a given link with content and title.

        :param link: href link for ``(#)`` tag.
        :param text: text content for description.
        """
        link = mistune.escape_link(link).replace(' ', '-')
        link = ''.join([c for c in link if c.isalpha() or c.isalnum() or c == '-'])
        link = link.lower()
        return '[%s](#%s)' % (text, link)


class Toci:

    def execute(self, notebook=None) -> str:
        assert notebook is not None, "the notebook is not valid"

        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)

        class MarkdownCell(Preprocessor):
            def preprocess_cell(self, cell, resources, index):
                if cell.cell_type == 'markdown':
                    markdown(cell.source)
                return cell, resources

        with open(notebook, encoding='utf-8') as fh:
            nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

        c = Config()
        c.NotebookExporter.preprocessors = [MarkdownCell]
        exporter = NotebookExporter(config=c)
        _, _ = exporter.from_notebook_node(nb)

        return renderer.render_toc()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='toci 0.0.1')
    parser.add_argument('--notebook', '-n', required=True, help="an ipynb notebook file")
    args = parser.parse_args(sys.argv[1:])

    toci = Toci()
    print(toci.execute(args.notebook))


if __name__ == '__main__':
    main()
