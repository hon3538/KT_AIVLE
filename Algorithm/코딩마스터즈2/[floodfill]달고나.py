'''
신입사원 종구는 달고나를 너무 좋아해서 매일 엄청난 양의 달고나를 먹습니다.
결국 종구는 참지 못하고 직접 달고나를 해먹고자 달고나 판을 구매했습니다. 
종구가 구매한 달고나 판은 다양한 크기의 구멍이 여러개 있습니다.

달고나를 만들 때는 판 전체에 설탕물을 부어야 하고,
달고나 판의 특성상 두 구멍이 상하좌우로 붙어있으면 하나의 달고나로 합쳐집니다. 

달고나 판의 구멍들의 위치가 주어지면, 
달고나를 한 번 만들 때 몇 개의 달고나가 만들어지는지 출력하는 프로그램을 작성하세요.

[입력]
첫 번째 줄에 달고나 판의 세로 길이 N과 가로 길이 M이 주어집니다. (1 ≤ N, M ≤ 100)
두 번째 줄부터 N+1번째 줄까지 0과 1로 달고나 판의 형태가 주어집니다. 구멍이 뚫린 곳은 0, 막혀있는 곳은 1입니다.
5 5
00100
00100
11111
00100
00100

[출력]
달고나를 한 번 만들 때 몇 개의 달고나가 만들어지는지 출력합니다.
'''
'''
[전략]
flood fill 로 탐색, 구간 탐색 횟수 = 달고나 개수
'''
import queue


N, M = 0, 0
hole_map = []
visited = [[False]*100 for _ in range(100)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서 (y, x)

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

def bfs(y, x):
    global hole_map, N, M, dir, visited
    q = queue.Queue()

    visited[y][x] = True
    q.put(Node(y, x))

    while not q.empty():
        node = q.get()

        for i in range(4):
            dy = node.y + dir[i][0]
            dx = node.x + dir[i][1]

            if (dy < 0) | (dx < 0) | (dy >= N) | (dx >= M):
                continue

            if (hole_map[dy][dx] != '0') | (visited[dy][dx] == True):
                continue
            
            visited[dy][dx] = True
            q.put(Node(dy, dx))


N, M = map(int, input().split())  # 달고나 판의 세로길이, 가로길이

for i in range(N):
    s = input()
    hole_map.append(s)

cnt = 0
for y in range(N):
    for x in range(M):
        if (hole_map[y][x] != '0') | (visited[y][x] == True):
            continue
        bfs(y, x)
        cnt += 1

print(cnt)
