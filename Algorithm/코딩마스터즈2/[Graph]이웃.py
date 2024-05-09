'''
N개의 정점과 M개의 양방향 간선으로 이루어진 그래프가 주어집니다.
정점에는 1번부터 N번까지 번호가 붙어있습니다. 
또한, 정점마다 가중치가 부여되어 있습니다. 
어떤 정점 하나를 선택하고 해당 정점의 가중치를 1 높일 때마다 비용이 1만큼 발생합니다.

그래프의 모든 이웃한 정점 간 가중치 차이를 K 이하가 되도록 만들기 위해 필요한 최소 비용을 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 정점의 개수 N, 간선의 개수 M, 가중치 차이 K가 공백으로 구분되어 주어집니다. (2 ≤ N ≤ 50, 1 ≤ M ≤ 200, 1 ≤ K ≤ 100)

이어서 N개의 줄에 걸쳐 i번 정점의 가중치를 의미하는 양의 정수 s가 주어집니다. (1 ≤ s ≤ 1,000)

이어서 M개의 줄에 걸쳐 간선의 정보를 의미하는 양의 정수 u, v가 주어집니다.
이는 u번 정점과 v번 정점을 연결하는 간선이 존재함을 의미합니다.
즉, u번 정점과 v번 정점이 이웃합니다.

[출력]
그래프의 모든 이웃한 정점 간 가중치 차이를 K 이하가 되도록 만들기 위해 필요한 최소 비용을 출력합니다.
'''
'''
[설계]
비용을 추가하여 가중치를 높이는 경우밖에 없기 때문에, 높은 순서로 순회한다.
각 정점을 가중치가 높은 순서부터 순회하면서, 주변 정점들의 가중치를 K개만큼 차이날 때까지 높인다.
pq를 사용하여 업데이트를 시키더라도 높은 순서대로 순회할 수 있도록 한다.

모든 그래프가 연결되어 있지 않을 가능성
-> 처음에 pq에 다 집어넣음, pq에서 꺼낸 노드와 이웃인 노드들은 visited
-> update된 애들만 pq에 다시 넣어줌

'''
import queue

def explore_graph(start, K):
    global vector, visited, weights, pq
    ans = 0
    
    
    while not pq.empty():
        w, node = pq.get()
        w = -w

        visited[node] = True
        
        for next in vector[node]:
            if visited[next]:
                continue
            
            if w - weights[next] > K:  # 업데이트 필요한 애들
                cost = w - weights[next] - K
                ans += cost

                weights[next] = weights[next] + cost
                pq.put((-weights[next], next))

            visited[next] = True
    
    return ans


N, M, K = map(int, input().split())  # 노드 개수, 간선 개수, 가중치 차이
vector = [[] for _ in range(N+1)]
weights = [-1,]

visited = [False]*(N+1)
pq = queue.PriorityQueue()

max_weight = -1
max_index = -1
for i in range(N):
    w = int(input())
    weights.append(w)
    pq.put((-w, i+1))


for _ in range(M):
    u, v = map(int, input().split())  # 시작, 끝
    vector[u].append(v)
    vector[v].append(u)

result = explore_graph(max_index, K)
print(result)
