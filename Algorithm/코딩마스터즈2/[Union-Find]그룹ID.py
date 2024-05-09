'''
철수의 마을에는 총 N명의 사람이 존재하고, 각 사람에게는 1번부터 N번까지 번호가 붙어있습니다.
철수는 마을 사람들의 친구 관계를 그래프로 모델링했습니다. 그래프의 정점은 N개이고, 간선은 M개입니다. 

각 정점에는 1번부터 N번까지 번호가 붙어있습니다. i번 사람은 i번 정점에 대응합니다. 간선은 양방향입니다.
u번 정점과 v번 정점을 잇는 간선이 존재하는 경우, u번 사람과 v번 사람이 친구임을 의미합니다.

마을의 각 사람은 정확히 하나의 그룹에 속합니다.
u번 정점에서 v번 정점으로 가는 경로가 존재하는 경우, u번 사람과 v번 사람이 같은 그룹에 속함을 의미합니다.
그룹의 ID는 해당 그룹에 포함된 사람들의 번호 중 가장 작은 번호입니다.

마을에 존재하는 그룹 중 가장 많은 사람이 포함된 그룹의 ID를 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 N과 M이 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 100, 1 ≤ M ≤ 500)
이어서 M개의 줄에 거쳐 마을 사람들의 친구 관계가 주어집니다. 각 줄에는 양의 정수 u, v가 공백으로 구분되어 주어집니다. 
이는 u번 정점과 v번 정점을 잇는 간선이 존재함을 의미합니다. (1 ≤ u, v ≤ N, u ≠ v)

[출력]
첫째 줄에 가장 많은 사람이 포함된 그룹의 ID를 출력합니다. 단, 조건을 만족하는 그룹이 여러 개인 경우 그 중 가장 작은 ID를 출력합니다.
'''
'''
[설계]
Union Find 
'''

def Find(node):
    global parrent
    if parrent[node] == node:
        return node
    
    parrent[node] = Find(parrent[node])
    return parrent[node]

def Union(A, B):
    global parrent, population

    pa = Find(A)
    pb = Find(B)
    if pa == pb:
        return
    
    if pa > pb :  # pa를 더 작게하기 위해 swap
        pa = pa^pb
        pb = pa^pb
        pa = pa^pb

    population[pa] += population[pb]    
    parrent[B] = pa

parrent = list(range(0, 101))
population = [1]*101

graph = [[] for _ in range(101)]
N, M = map(int, input().split())
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N+1):
    for to in graph[i]:
        Union(i, to)
ans = 0
max_val = 0
for i, p in enumerate(population):
    if max_val < p:
        max_val = p
        ans = i
print(ans)