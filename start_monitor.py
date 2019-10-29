#!/usr/bin/python3

import argparse
from monitor import TcpmirrorMonitor
from config import Config
import os


def analyze(filename):
    try:
        config = Config(filename)
        monitor = TcpmirrorMonitor(config)
        monitor.start()
    except Exception as err:
        print("ERROR: can't get info about", filename, ":", err)

parser = argparse.ArgumentParser()
parser.add_argument("path", help="a file of a path to files")
args = parser.parse_args()
if os.path.isdir(args.path):
    for file in os.listdir(args.path):
        if file.endswith(".toml"):
            analyze(file)
elif os.path.isfile(args.path) and args.path.endswith(".toml"):
    analyze(args.path)
else:
    print("ERROR: invalid file or path to a files")
