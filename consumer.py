class Consumer:
    def __init__(self, key, data):
        system = data[key]
        self.name = key
        self.address = system['address']
        self.protocol = system['protocol']
        self.id = system['id']

    def name(self):
        return self.name + " (" + self.protocol + ")"
