'''
너비가 W, 높이가 H인 평면에 한 변의 길이가 1인 정육면체 주사위가 있습니다.
여러분은 쿼리에 따라 이 주사위를 굴려야 합니다. 

주사위가 매번 구를 때마다 주사위와 맞닿는 바닥에는 그 주사위의 바닥에 있는 숫자가 찍히게 됩니다. 
이때, 주사위를 굴리기 전에는 주사위의 바닥면이 평면에 맞닿습니다.
어떤 바닥면에 두 번 이상 지나가는 경우에는 맨 마지막으로 맞닿은 면으로 갱신됩니다. 

주사위를 굴릴 때는 한 칸씩 구르는 방향으로 이동하면서 구르게 되지만 
주어진 평면을 벗어나는 움직임일 경우 제자리에서 구르게 됩니다. 
제자리에서 구른 이후에는 바닥면과 맞닿은 주사위면으로 갱신됩니다. 

평면의 너비와 높이, 주사위의 최초 상태, 주사위를 굴린 방법이 주어졌을때,
주사위를 굴린 후 평면에 찍혀있을 숫자를 알아내는 프로그램을 작성하세요. 

[입력]
첫 번째 줄에 평면의 너비를 의미하는 정수 W와 높이를 의미하는 H가 주어집니다. (1 ≤ W, H ≤ 10)

두 번째 줄에 주사위의 위치를 의미하는 정수 X, Y가 주어집니다.
이는 평면의 (0, 0)으로부터 동쪽으로 X칸, 남쪽으로 Y칸 떨어져있음을 의미합니다. (0 ≤ X < W, 0 ≤ Y < H)

세 번째 줄에 100 이하의 자연수가 6개 주어집니다.
첫 번째 정수부터 차례로 주사위의 동쪽면, 남쪽면, 서쪽면, 북쪽면, 위쪽면, 바닥면에 쓰인 숫자를 의미합니다.

네 번째 줄에 주사위를 굴린 횟수 N이 주어집니다. (1 ≤ N ≤ 50)

다섯 번째 줄에 주사위를 굴린 방법을 의미하는 4 이하의 자연수가 공백으로 구분되어 N개 주어집니다.
1은 동쪽, 2는 남쪽, 3은 서쪽, 4는 북쪽을 의미합니다.

'''
def tumble(dir):
    global east, south, west, north, top, bottom, Map

    if dir == 1:  # 동쪽
        east, top, west, bottom = top, west, bottom, east
    elif dir == 2:  # 남쪽
        south, top, north, bottom = top, north, bottom, south    
    elif dir == 3:  # 서쪽
        west, top, east, bottom = top, east, bottom, west 
    else:  # 북쪽
        north, top, south, bottom = top, south, bottom, north 

W, H = map(int, input().split())  # 너비, 높이
X, Y = map(int, input().split())  # 주사위의 현재 위치
east, south, west, north, top, bottom = map(int, input().split())  # 각 면에 쓰인 숫자
N = int(input())  # 주사위 굴릴 횟수
dice_directs = list(map(int, input().split()))  # 1 동쪽, 2 남쪽, 3 서쪽, 4 북쪽 방향으로 밀다.

Map = [[0]*W for _ in range(H)]
Map[Y][X] = bottom

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 동 남 서 북 x, y
for d in dice_directs:
    tumble(d)
    dx = X + dirs[d-1][0]
    dy = Y + dirs[d-1][1]
    
    if not ((dx < 0) | (dy < 0) | (dx >= W) | (dy >= H)):  # 이돌할 위치가 Map 범위 안에 들었다면 옮기기
        X, Y = dx, dy
        
    Map[Y][X] = bottom
        
        
        
for y in range(H):
    for x in range(W):
        print(Map[y][x], end=' ')
    print()
        

