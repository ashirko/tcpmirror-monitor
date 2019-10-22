#!/usr/bin/python3

import argparse
from monitor import TcpmirrorMonitor
from config import Config

parser = argparse.ArgumentParser()
parser.add_argument("path", help="a path to a file of files")
args = parser.parse_args()
config = Config(args.path)
monitor = TcpmirrorMonitor(config)
monitor.start()
