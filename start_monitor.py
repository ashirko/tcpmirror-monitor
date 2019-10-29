#!/usr/bin/python3

import argparse
from analyzer import Analyzer

parser = argparse.ArgumentParser()
parser.add_argument("path", help="a file of a path to files")
args = parser.parse_args()
a = Analyzer(args.path)
a.start()
