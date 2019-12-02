import json

class Node(object):
    def __init__(self, name, parents, destinations, data):
        self.name = name
        self.data = data
        self.parents = parents
        self.children = []
        self.destinations = destinations
        self.visited = False
        self.examined = False

    def ___str___(self):
        return self.name
