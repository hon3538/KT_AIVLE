'''
[설계]
도시 개수 1000, 간선 개수 3000

S -> K
K -> N

dijkstra 두 번 돌리기
도시 탐색 1000번 + 간선 탐색 (3000log3000)*2 = 6만정도
'''
import queue
from re import S

class Node:
    def __init__(self, to, w):
        self.to = to
        self.w = w

def dijkstra(start, end):
    dist = [0x7fffffff]*(N+1)

    pq = queue.PriorityQueue()
    pq.put((0, start))
    dist[start] = 0
    
    
    while not pq.empty():
        w, node = pq.get()
        
        if node == end:
            return w
        
        if dist[node] < w:
            continue
        
        for next in vector[node]:
            next_w = next.w + w
            if dist[next.to] <= next_w:
                continue
            
            dist[next.to] = next_w
            pq.put((next_w, next.to))
            
        
N, M, K = map(int, input().split())  # 도시 개수, 도로 개수, 자녀 학교 위치

vector = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    vector[u].append(Node(v, w))

ans = 0
ans += dijkstra(1, K)
ans += dijkstra(K, N)
print(ans)

