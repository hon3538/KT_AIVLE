'''
철수가 사는 동네는 N개의 구역과 M개의 단방향 도로로 구성되어 있습니다. 
각 구역에는 1번부터 N번까지 번호가 붙어있고, 철수는 1번 구역에 있습니다.

철수는 소화도 시킬 겸 동네를 산책하려고 합니다. 
그런데 도로들이 모두 단방향이므로, 
처음에 출발했던 구역으로 다시 돌아오지 못할 수도 있습니다.

구역과 도로들의 정보가 주어졌을 때, 
철수가 처음 출발했던 1번 구역으로 돌아올 수 있는지 판단하는 프로그램을 작성하세요. 

단, 1번 구역 외 다른 구역을 적어도 한번은 거쳐야 산책으로 인정됩니다.

[입력]
첫째 줄에 구역의 개수와 단방향 도로의 개수를 의미하는 양의 정수 N과 M이 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 100, 1 ≤ M ≤ 500)

이어서 M개의 줄에 걸쳐 단방향 도로의 시작 구역의 번호 s와 도착 구역의 번호 e가 주어집니다.
이는 해당 도로를 통해 s번 구역에서 e번 구역으로 이동할 수 있음을 의미합니다.
단, s ≠ e이며 s번 구역에서 e번 구역으로 향하는 간선은 단 하나만 존재합니다.

[출력]
다른 구역을 거쳐 1번 구역으로 돌아올 수 있으면 “YES”, 돌아올 수 없으면 “NO”를 출력합니다.
'''
'''
[설계]
그냥 그래프 문제, 순회하면서 1번으로 들어가는지 확인
'''
import queue

def explore_graph(start):
    global visited, vector
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        node = q.get()

        for next in vector[node]:
            if visited[next]:
                continue
            
            visited[next] = True
            
            if next == start:
                return True
            
            q.put(next)

    return False

N, M = map(int, input().split())  # 노드 수, 간선 수

vector = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    s, e = map(int, input().split())  # 시작지점, 도착지점
    vector[s].append(e)

if explore_graph(1):
    print('YES')
else:
    print('NO')