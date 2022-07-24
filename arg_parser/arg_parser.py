"""
Usage:
    oi.py [--selector SELECTOR] <query>...
    oi.py --list-selectors

Options:
    -s --selector SELECTOR  specify selector to apply
    -l --list-selectors     list available selectors
"""

from docopt import docopt


def get_args():
    print(docopt(__doc__))
    return docopt(__doc__)
