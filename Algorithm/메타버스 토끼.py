'''
달리기 시합의 승자는 미로의 맨 위 왼쪽 칸(1행 1열)에서 출발해 미로의 맨 아래 오른쪽 칸(N행 M열)에 먼저 도착하는 쪽입니다. 
미로의 각 칸은 벽 또는 빈 칸으로, 토끼와 거북이 모두 벽을 넘거나 부술 수 없습니다. 
미로의 테두리(1행의 위, N행의 아래, 1열의 왼쪽, M열의 오른쪽)는 모두 벽으로 막혀 있습니다.

토끼는 1분에 한 번 상하좌우 중 한 방향으로 최대 2칸 이동합니다. 

토끼의 이동을 조금 더 자세하게 서술하겠습니다. 
우선 이동할 방향을 정하고, 1칸 이동합니다. 
같은 방향으로 1칸 더 이동할 수 있다면 반드시 이동해야 하며, 아니라면 거기서 멈춥니다. 
첫 번째 예시 입력을 예로 들면, 토끼 로봇이 오른쪽 - 아래 - 오른쪽 순으로 이동할 때 그의 위치는 1행 1열 - 1행 2열 - 3행 2열 - 3행 4열 순입니다.

미로의 모습이 입력으로 주어집니다. 
토끼가 미로의 맨 위 왼쪽 칸에서 출발해 미로의 맨 아래 오른쪽 칸으로 이동하는데 적어도 몇 분이 걸리는지 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 미로의 세로 너비 N과 가로 너비 M이 주어집니다. (2 ≤ N ≤ 50, 2 ≤ M ≤ 50)

둘째 줄부터 N개의 줄에 걸쳐 미로의 정보가 주어집니다.
#는 벽을 나타내며, .는 빈 칸을 나타냅니다.

[출력]
토끼가 미로의 맨 위 왼쪽 칸에서 출발해 미로의 맨 아래 오른쪽 칸으로 이동하는데 몇 분이 걸리는지 출력합니다.
어떻게 이동해도 맨 아래 오른쪽 칸에 도달하지 못한다면 대신 -1을 출력합니다.

[설계]
단순 bfs
Node를 (time, y, x) 로 만들고 진행
'''
import queue
class Node:
    def __init__(self, time, y, x):
        self.time = time
        self.y = y
        self.x = x
        
def is_possible(y, x):
    global MAP, N, M
    
    if (y < 0) | (x < 0) | (y >=N) | (x >= M):
        return False
    
    if MAP[y][x] == '#':
        return False
    
    return True
    
def bfs():
    global dir, N, M, visited
    q = queue.Queue()
    q.put(Node(0, 0, 0))
    visited[0][0] = True
    
    while not q.empty():
        node = q.get()

        if (node.y == N-1) & (node.x == M-1):
            return node.time
        
        for i in range(4):
            dy = node.y + dir[i][0]
            dx = node.x + dir[i][1]
            
            if not is_possible(dy, dx):
                continue
            
            if is_possible(dy + dir[i][0], dx + dir[i][1]):
                dy += dir[i][0]
                dx += dir[i][1]
            
            if visited[dy][dx] :
                continue
            
            visited[dy][dx] = True
            q.put(Node(node.time + 1, dy, dx))
            
    return -1

N, M = map(int, input().split())  # 행, 열
MAP = []

visited = [[False]*M for _ in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동 남 서 북

for _ in range(N):
    MAP.append(input())

ans = bfs()
print(ans)
