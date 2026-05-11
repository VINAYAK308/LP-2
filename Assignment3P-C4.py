# Implement Following Greedy search algorithm - Prim's Minimal Spanning Tree Algorithm
import heapq

def primMST(V, adj):
    # Min-heap (weight, node)
    pq = []
    heapq.heappush(pq, (0, 0))

    inMST = [False] * V
    total_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if inMST[node]:
            continue

        inMST[node] = True
        total_weight += weight

        for adjNode, edgeWeight in adj[node]:
            if not inMST[adjNode]:
                heapq.heappush(pq, (edgeWeight, adjNode))

    print("Total weight of MST:", total_weight)


def main():
    V = 5
    adj = [[] for _ in range(V)]

    adj[0].append((1, 2))
    adj[1].append((0, 2))

    adj[0].append((3, 6))
    adj[3].append((0, 6))

    adj[1].append((2, 3))
    adj[2].append((1, 3))

    adj[1].append((3, 8))
    adj[3].append((1, 8))

    adj[1].append((4, 5))
    adj[4].append((1, 5))

    adj[2].append((4, 7))
    adj[4].append((2, 7))

    primMST(V, adj)


if __name__ == "__main__":
    main()

# python3 Assignment3.py
# Total weight of MST: 16
 