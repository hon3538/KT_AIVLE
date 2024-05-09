'''
3x3 체스판에 흰색 나이트 2개와 검정 나이트 2개가 주어집니다.
모든 흰색과 검정색 나이트의 위치를 서로 바꿀 수 있는지 판단해주는 프로그램을 작성하세요.

나이트의 이동 규칙은 다음과 같습니다.
편의상 체스판을 직교 좌표계로 나타내어 어떤 나이트가 (x, y)에 위치한다고 가정합시다.
그러면 그 나이트는 다음 8개의 좌표들 중 다른 기물이 없는 체스판 위로 이동할 수 있습니다.
(x-1, y+2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x+2, y-1), (x+2, y+1), (x-1, y-2), (x+1, y-2)

[입력]
첫째줄 부터 3줄에 걸쳐 현재 체스판의 상태가 주어집니다
0은 빈칸, 1은 흰색 나이트, 2는 검정 나이트를 의미합니다.

[출력]
흰색과 검정색 나이트의 자리를 바꿀 수 있으면 “possible”, 바꿀 수 없으면 “impossible”을 출력합니다.
'''
'''
[설계]
검정말이 흰색 말을 각각 잡을 수 있는 지와 같은 말.
각각 visit map을 가지고 bfs 로 탐색, 더이상 가본 곳이 없을 때까지 반복
'''
import queue


def bfs(start):
    global chess_map, dir, white
    q = queue.Queue()
    q.put((start[0], start[1]))
    visited = [[False]*3 for _ in range(3)]
    visited[start[1]][start[0]] = True
    
    while not q.empty():
        now_x, now_y = q.get()

        if (now_x*10 + now_y) in white:
            white.remove(now_x*10 + now_y)
            return
        
        for i in range(8):
            dx = now_x + dir[i][0]
            dy = now_y + dir[i][1]

            if (dy<0) | (dx<0) | (dy>=3) | (dx>=3):
                continue

            if visited[dy][dx]:
                continue
            visited[dy][dx] = True

            q.put((dx, dy))

chess_map = []
for _ in range(3):
    chess_map.append(input())

black = []
white = set()
for y in range(3):
    for x in range(3):
        if chess_map[y][x] == '1':
            black.append((x,y))
        if chess_map[y][x] == '2':
            white.add(x*10+y)

visited = []    
dir = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1), (-1, -2), (1, -2)]  # x, y 좌표다

bfs(black[0])
bfs(black[1])

if len(white) == 0:
    print('possible')
else:
    print('impossible')

