import os
import toml


class Config:
    def __init__(self, file_name):
        data = toml.load(file_name)
        self.file_name = file_name
        name = os.path.splitext(os.path.basename(self.file_name))
        self.name = name[0]
        self.listen_address = data['listen_address']
        self.listen_protocol = data['listen_protocol']
        consumers = data['consumers_list']
        self.consumers = []
        for key in consumers:
            consumer = Consumer(key, data)
            self.consumers.append(consumer)


class Consumer:
    def __init__(self, key, data):
        system = data[key]
        self.name = key
        self.address = system['address']
        self.protocol = system['protocol']
