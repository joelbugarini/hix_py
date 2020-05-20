class ParserNode():
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj, type):
        self.children.append(obj)