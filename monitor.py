import subprocess
from prettytable import PrettyTable
import psutil


class TcpmirrorMonitor:
    def __init__(self, config):
        self.config = config

    def start(self):
        table = PrettyTable()
        table.field_names = self.field_names()
        data = self.data()
        table.add_row(data)
        print(table)

    def field_names(self):
        sources = "sources (" + self.config.listen_protocol + ")"
        consumers = []
        for consumer in self.config.consumers:
            consumer_name = consumer.name + " (" + consumer.protocol + ")"
            consumers.append(consumer_name)
        return [sources] + consumers

    def data(self):
        pid = self.get_pid()
        p = psutil.Process(pid)
        connections = p.connections()
        sources = self.get_connections(self.config.listen_address, connections)
        consumers = []
        for consumer in self.config.consumers:
            consumer_data = self.get_connections(consumer.address, connections)
            consumers.append(consumer_data)
        return [sources] + consumers

    def get_connections(self, address, connections):
        [ip, port] = address.split(":")
        port = int(port)
        if ip == 'localhost' or ip == "":
            num = self.get_connections_from_local(connections, port)
        else:
            num = self.get_connections_to_remote(connections, ip, port)
        return num

    @staticmethod
    def get_connections_from_local(connections, port):
        num = 0
        for connection in connections:
            a = connection.laddr
            if len(a) == 2 and a.port == port and\
                    connection.status == 'ESTABLISHED':
                num += 1
        return num

    @staticmethod
    def get_connections_to_remote(connections, ip, port):
        num = 0
        for connection in connections:
            a = connection.raddr
            if len(a) == 2 and a.ip == ip and a.port == port and\
                    connection.status == 'ESTABLISHED':
                num += 1
        return num

    def get_pid(self):
        pid = int(subprocess.check_output(["pgrep", "-fo",  self.config.file_name]))
        return pid
