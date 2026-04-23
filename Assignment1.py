from collections import deque

def dfs(node, adj, visited):
    visited[node] = True
    print(node, end=" ")

    for nbr in adj[node]:
        if not visited[nbr]:
            dfs(nbr, adj, visited)


def bfs(start, adj, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nbr in adj[node]:
            if not visited[nbr]:
                visited[nbr] = True
                q.append(nbr)


def main():
    V = 5
    adj = [[] for _ in range(V)]

    # Undirected graph
    adj[0].append(1)
    adj[1].append(0)

    adj[0].append(2)
    adj[2].append(0)

    adj[1].append(3)
    adj[3].append(1)

    adj[2].append(4)
    adj[4].append(2)

    visited = [False] * V

    print("DFS :", end=" ")
    dfs(0, adj, visited)

    print("\nBFS :", end=" ")

    # Reset visited for BFS
    visited = [False] * V
    bfs(0, adj, visited)

    print()


if __name__ == "__main__":
    main()

# python3 Assignment1.py 
# DFS : 0 1 3 2 4 
# BFS : 0 1 2 3 4 