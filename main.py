
from collections import deque

# ==========================================
# ASSESSMENT 3.4
# NON-LINEAR DATA STRUCTURE
# Name: ABAYATA
# ==========================================


# ==========================================
# PART 1: BINARY TREE
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Binary Tree BFS
def tree_bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("Binary Tree BFS:")

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print()


# Binary Tree DFS (Preorder)
def tree_dfs(root):
    if root is None:
        return

    print(root.data, end=" ")

    tree_dfs(root.left)
    tree_dfs(root.right)


# Create Binary Tree using ABAYATA
A1 = Node("A1")
B = Node("B")
A2 = Node("A2")
Y = Node("Y")
A3 = Node("A3")
T = Node("T")
A4 = Node("A4")

A1.left = B
A1.right = A2

B.left = Y
B.right = A3

A2.left = T
A2.right = A4


# ==========================================
# PART 2: GRAPH
# ==========================================

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].append(vertex2)
        self.vertices[vertex2].append(vertex1)

    # Graph BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        print("Graph BFS:")

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.vertices[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

    # Graph DFS
    def dfs(self, start):
        visited = set()

        print("Graph DFS:")

        def traverse(vertex):
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    traverse(neighbor)

        traverse(start)
        print()


# Create Graph using ABAYATA
graph = Graph()

letters = ["A1", "B", "A2", "Y", "A3", "T", "A4"]

for letter in letters:
    graph.add_vertex(letter)

# Connect the vertices
graph.add_edge("A1", "B")
graph.add_edge("A1", "A2")
graph.add_edge("B", "Y")
graph.add_edge("B", "A3")
graph.add_edge("A2", "T")
graph.add_edge("A2", "A4")


# ==========================================
# PART 3: MAIN PROGRAM
# ==========================================

def main():

    print("======================================")
    print("       ABAYATA DATA STRUCTURE")
    print("          ASSESSMENT 3.4")
    print("======================================")

    print("\n[ BINARY TREE ]")

    tree_bfs(A1)

    print("Binary Tree DFS:")
    tree_dfs(A1)
    print()

    print("\n[ GRAPH ]")

    graph.bfs("A1")
    graph.dfs("A1")

    print("\n======================================")
    print("          END OF PROGRAM")
    print("======================================")


if __name__ == "__main__":
    main()
