from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = [0] * (n + 1)
        graph = defaultdict(set)
        
        # Build degree count and adjacency sets
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            graph[u].add(v)
            graph[v].add(u)
        
        # Collect odd-degree nodes
        odd_nodes = [i for i in range(1, n+1) if deg[i] % 2 == 1]
        m = len(odd_nodes)
        
        if m == 0:
            return True  # All degrees already even
        elif m == 2:
            u, v = odd_nodes
            # Can we connect the two odd nodes directly?
            if v not in graph[u]:
                return True
            # Check if there's a third node to connect both
            for x in range(1, n+1):
                if x != u and x != v and x not in graph[u] and x not in graph[v]:
                    return True
            return False
        elif m == 4:
            a, b, c, d = odd_nodes
            # Check all pairing options (max 2 edges)
            pairs = [
                ((a,b),(c,d)),
                ((a,c),(b,d)),
                ((a,d),(b,c))
            ]
            for (p1,p2) in pairs:
                if p1[1] not in graph[p1[0]] and p2[1] not in graph[p2[0]]:
                    return True
            return False
        else:
            return False