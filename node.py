import json

class Node(object):
    def __init__(self, name, parents, destinations, data):
        self.name = name
        self.data = data
        self.parents = parents
        self.children = []
        self.destinations = destinations

    def ___str___(self):
        return self.name
