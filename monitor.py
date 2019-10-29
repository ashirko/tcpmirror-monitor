import subprocess
from prettytable import PrettyTable
import psutil


class TcpmirrorMonitor:
    def __init__(self, config):
        self.config = config

    def start(self):
        self._print_table()

    def _print_table(self):
        table = PrettyTable()
        table.field_names = self._field_names()
        data = self._data()
        table.add_row(data)
        print(table)

    def _field_names(self):
        sources = "sources (" + self.config.listen_protocol + ")"
        consumers = []
        for consumer in self.config.consumers:
            consumer_name = consumer.name + " (" + consumer.protocol + ")"
            consumers.append(consumer_name)
        return [sources] + consumers

    def _data(self):
        pid = self._get_pid()
        p = psutil.Process(pid)
        connections = p.connections()
        sources = self._get_connections(self.config.listen_address, connections)
        consumers = []
        for consumer in self.config.consumers:
            consumer_data = self._get_connections(consumer.address, connections)
            consumers.append(consumer_data)
        return [sources] + consumers

    def _get_connections(self, address, connections):
        [ip, port] = address.split(":")
        port = int(port)
        if ip == 'localhost' or ip == "":
            num = self._get_connections_from_local(connections, port)
        else:
            num = self._get_connections_to_remote(connections, ip, port)
        return num

    def _get_pid(self):
        pid = int(subprocess.check_output(["pgrep", "-fo",  self.config.file_name]))
        return pid

    @staticmethod
    def _get_connections_from_local(connections, port):
        num = 0
        for connection in connections:
            a = connection.laddr
            if len(a) == 2 and a.port == port and\
                    connection.status == 'ESTABLISHED':
                num += 1
        return num

    @staticmethod
    def _get_connections_to_remote(connections, ip, port):
        num = 0
        for connection in connections:
            a = connection.raddr
            if len(a) == 2 and a.ip == ip and a.port == port and\
                    connection.status == 'ESTABLISHED':
                num += 1
        return num
