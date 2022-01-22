# Toci

Toci is a markdown tool to generate an outline from a given Jupyter notebook. It traverses the markdown cells of a given `ipynb` file to form a toc for you.

## How it works

```
$ pip install toci==0.0.3

$ toci --help
usage: toci [-h] [--version] --notebook NOTEBOOK

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --notebook NOTEBOOK, -n NOTEBOOK
                        an ipynb notebook file
```

Create a table of content from a given ipynb file as follows:

```
$ toci -n notebook.ipynb                                                                                                      
# Table of Content
- [Intro](#intro)
  - [Heading 2](#heading-2)
    - [Heading 3](#heading-3)
  - [Another Heading 2](#another-heading-2)
  - [Another Heading 2 2](#another-heading-2-2)
    - [Another Heading 3](#another-heading-3)
      - [Another Heading 4](#another-heading-4)
- [😽 Cat Section](#-cat-section)
  - [is another section ready?](#is-another-section-ready)
```

## LICENSE

MIT


