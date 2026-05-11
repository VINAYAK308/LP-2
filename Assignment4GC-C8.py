# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for a graph coloring problem.

# Graph Coloring using Backtracking and Branch & Bound
# Colors: Red, Green, Blue

class GraphColoring:

    def __init__(self, vertices, num_colors):
        self.V = vertices
        self.num_colors = num_colors

        # Adjacency Matrix
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

        # Color assignment
        self.colors = [0] * vertices

        # Color Names
        self.color_names = ["Red", "Green", "Blue"]

    # Add edge in undirected graph
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    # Check whether color can be assigned
    def is_safe(self, node, color):

        for neighbor in range(self.V):

            if self.graph[node][neighbor] == 1 and self.colors[neighbor] == color:
                return False

        return True

    # Backtracking + Branch and Bound
    def solve(self, node=0):

        # All vertices colored
        if node == self.V:
            return True

        # Try all colors
        for color in range(1, self.num_colors + 1):

            # Branch Condition
            if self.is_safe(node, color):

                # Assign color
                self.colors[node] = color

                # Recursive call
                if self.solve(node + 1):
                    return True

                # Backtracking
                self.colors[node] = 0

        return False

    # Print graph structure
    def print_graph(self):

        print("\nGraph Structure:")

        for i in range(self.V):
            print(f"{i} --> ", end="")

            for j in range(self.V):
                if self.graph[i][j] == 1:
                    print(j, end=" ")

            print()

    # Print final coloring solution
    def print_solution(self):

        print("\nVertex Coloring Solution:")

        for i in range(self.V):
            print(f"Vertex {i} ---> {self.color_names[self.colors[i]-1]}")


def main():

    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    gc = GraphColoring(vertices, 3)

    print("\nEnter edges (u v):")

    for i in range(edges):

        u, v = map(int, input().split())

        gc.add_edge(u, v)

    # Display graph
    gc.print_graph()

    # Solve Graph Coloring
    if gc.solve():

        print("\nSolution Exists!")
        gc.print_solution()

    else:
        print("\nNo solution exists using Red, Green, Blue colors.")


if __name__ == "__main__":
    main()

# Sample Input
# Enter number of vertices: 4
# Enter number of edges: 4

# Enter edges (u v):
# 0 1
# 0 2
# 1 2
# 2 3
# Graph Structure
# 0 --> 1 2
# 1 --> 0 2
# 2 --> 0 1 3
# 3 --> 2
# Sample Output
# Solution Exists!

# Vertex Coloring Solution:
# Vertex 0 ---> Red
# Vertex 1 ---> Green
# Vertex 2 ---> Blue
# Vertex 3 ---> Red