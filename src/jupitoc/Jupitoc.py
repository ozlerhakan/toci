import argparse
import nbformat
import mistune

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
            content += ('' if level == 1 else '\t' * (level - 1)) + '- ' + self._link(text, text)
            content += '\n'
        return content

    def _link(self, link, text):
        """Rendering a given link with content and title.

        :param link: href link for ``(#)`` tag.
        :param text: text content for description.
        """
        link = mistune.escape_link(link).replace(' ', '-')
        title = mistune.escape(text, quote=False)
        return '[%s](#%s)' % (title, link)


class Toci:

    def execute(self, params):
        renderer = HighlightRenderer()
        markdown = mistune.Markdown(renderer=renderer)

        class MarkdownCell(Preprocessor):
            def preprocess_cell(self, cell, resources, index):
                if cell.cell_type == 'markdown':
                    markdown(cell.source)
                return cell, resources

        with open(params.notebook_path) as fh:
            nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

        c = Config()
        c.NotebookExporter.preprocessors = [MarkdownCell]
        exporter = NotebookExporter(config=c)
        _, _ = exporter.from_notebook_node(nb)

        print(renderer.render_toc())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='solring 0.0.2')
    args = parser.parse_args(sys.argv[1:])
    toci = Toci()
    toci.execute(args)


if __name__ == '__main__':
    main()
