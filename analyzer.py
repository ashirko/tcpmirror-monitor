from monitor import TcpmirrorMonitor
from config import Config
import os


class Analyzer:
    def __init__(self, path):
        self.path = path

    def start(self):
        if os.path.isdir(self.path):
            for file in os.listdir(self.path):
                if file.endswith(".toml"):
                    self.analyze(self.path + "/" + file)
        elif os.path.isfile(self.path) and self.path.endswith(".toml"):
            self.analyze(self.path)
        else:
            print("ERROR: invalid file or path to a files")

    @staticmethod
    def analyze(filename):
        try:
            config = Config(filename)
            monitor = TcpmirrorMonitor(config)
            monitor.start()
        except Exception as err:
            print("ERROR: can't get info about", filename, ":", err)
