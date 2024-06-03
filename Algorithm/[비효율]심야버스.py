'''
서울의 각 동네를 정점(i, j)로 보았을 때, i에서 j로 가는 버스 노선이 존재하는지 알아보는 프로그램을 작성하세요.

[예제입력]
7
0 1 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 1 0 1 0 0
0 0 0 1 0 1 0
0 0 0 0 1 0 1
0 0 0 0 0 1 0

[예제출력]
1 1 0 0 0 0 0
1 1 0 0 0 0 0
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1
0 0 1 1 1 1 1

N <= 100
단순 bfs
'''
import queue

from numpy import busday_count
N = int(input())
bus_path_map = []
for _ in range(N):
    bus_path_map.append(list(map(int, input().split())))

bus_path = [[] for _ in range(N)]  # map이 아닌 list 형식으로 가지기
for start in range(N):
    for end in range(N):
        if start == end:
            continue
        if bus_path_map[start][end] == 1:
            bus_path[start].append(end)

for node in range(N):  # N 개의 노드부터 출발해서 가능한 경로에 1 check
    q = queue.Queue()
    q.put(node)
    visited = [False]*N
    visited[node] = True
    while not q.empty():
        now = q.get()
        
        for next in bus_path[now]:
            if visited[next]:
                continue
            visited[next] = True
            bus_path_map[now][next] = 1
            q.put(next)

for y in range(N):
    for x in range(N):
        print(bus_path_map[y][x], end=' ')
    print()