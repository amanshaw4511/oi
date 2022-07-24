"""
Usage:
    oi.py [--selector SELECTOR] <query>...
    oi.py --list-selectors

Options:
    -s --selector SELECTOR  specify selector to apply
    -l --list-selectors     list available selectors
"""

from typing import cast

from docopt import docopt


def get_args():
    return docopt(cast(str, __doc__))
