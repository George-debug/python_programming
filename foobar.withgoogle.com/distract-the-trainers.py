# blooming
# https://algorithms.discrete.ma.tum.de/graph-algorithms/matchings-blossom-algorithm/index_en.html

class Node:
    def __init__(self, id):
        # type: (int) -> None
        self.id = id
        self.next = set()  # type: list[Node]

    def add(self, *nodes):
        for node in nodes:
            self.next.add(node)

    def remove(self, *nodes):
        for node in nodes:
            if node in self.next:
                self.next.remove(node)

    # debug
    def __repr__(self):
        return f"Node({self.id})"
    __str__ = __repr__

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


next_blossom_id = -1


class Blossom(Node):
    def __init__(self, nodes):
        global next_blossom_id
        self.circuit = nodes
        super().__init__(next_blossom_id)
        next_blossom_id -= 1

        self.next = set()
        for node in nodes:
            self.add(*node.next)

            for next_node in node.next:
                next_node.remove(node)
                next_node.add(self)

        self.remove(self)

        # type: (list[Node], list[Node]) -> None

# https://en.wikipedia.org/wiki/Blossom_algorithm#Finding_an_augmenting_path


class TreeNode(Node):
    def __init__(self, id):
        super().__init__(id)
        self.next = [None] * 2  # type: list[TreeNode]

    def __repr__(self):
        return f"TreeNode({self.id})"
    __str__ = __repr__

    def get_length(self):
        left_length = 0 if self.next[0] is None else self.next[0].get_length()
        right_length = 0 if self.next[1] is None else self.next[1].get_length()

        return max(left_length, right_length) + 1


def print_graph(node):

    q = [node]
    visited = set()
    visited.add(node)
    while q:
        node = q.pop(0)
        print(node, " : ", node.next)
        for next_node in node.next:
            if next_node not in visited:
                q.append(next_node)
                visited.add(next_node)

# read from graph.txt


def redo_blossom(blossom):
    # type: (Blossom) -> None

    for node in blossom.circuit:
        for next_node in node.next:
            next_node.remove(blossom)
            next_node.add(node)


graph = {}

for line in open("graph.txt", "r"):
    a, b = map(int, line.split())

    if a not in graph:
        graph[a] = Node(a)
    if b not in graph:
        graph[b] = Node(b)

    graph[a].add(graph[b])
    graph[b].add(graph[a])


print_graph(graph[0])

print("\n    \n")
b = Blossom([graph[0], graph[1], graph[2]])
print_graph(graph[5])

print("\n    \n")
redo_blossom(b)
print_graph(graph[5])


print("\n    \n")
b = Blossom([graph[0], graph[1], graph[2]])
print_graph(graph[5])

print("\n    \n")
redo_blossom(b)
print_graph(graph[5])
