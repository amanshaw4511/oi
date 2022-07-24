"""
Usage:
    script_name.py [-a] [-b] <query>...

Options:
    -a            Print all the things.
    -b            Get more bees into the path.
"""
from docopt import docopt


def get_args():
    return docopt(__doc__)