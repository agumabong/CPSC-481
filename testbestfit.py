import heapq
class address():
    def __init__(self, address, distance, goto, parent, children):
        self.address = address
        self.distance = distance
        self.goto = goto
        self.parent = parent
        self.children = []

root = address("california", ["new york", "texas"], None, [x, y])
x = address("new york", ["texas"], "california", [])
y = address("texas", ["new york"], "california", [])

if len(root.goto) == 0:
    pop = heapq.heapop(self.open)