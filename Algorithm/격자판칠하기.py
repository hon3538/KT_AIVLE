'''
민규는 화장실 바닥을 바라보고 있었습니다. 
바닥은 격자판 모양이었고, 계속해서 바라보다 보니 이런 생각이 들었습니다.

세로 크기가 N이고, 가로 크기가 M인 격자판을 이웃한 격자는 같은 색으로 칠하지 않으면서 서로 다른 세 가지 색으로 칠하면 칠할 수 있는 경우의 수는 몇 개가 될까?

이때 이웃한 격자란 한 변을 공유하는 두 격자를 의미합니다.

격자의 크기가 주어질 때, 
이웃한 격자는 같은 색으로 칠하지 않으면서 격자를 서로 다른 세 가지 색으로 칠할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 자연수 N, M이 공백으로 구분되어 주어집니다.(1 ≤ N, M ≤ 5)

[출력]
이웃한 격자는 같은 색으로 칠하지 않으면서 격자를 서로 다른 네 가지 색으로 칠할 수 있는 경우의 수를 출력합니다.

[설계]
dfs 2^25 = 3200만..
'''
def dfs(level, color):  # level ~24
    global N, M, color_map
    if level == (N*M-1):  # level 0에 1개가 완성되어있어, level 24면 25개가 완성되어 있어 
        return 1
    
    y = int(level/M)
    x = int(level%M)
    color_map[y][x] = color
    
    # set에 있는 값 하나씩 넣고 재귀
    cnt = 0
    for color in [1, 2, 3]:
        # 위 확인
        dy = int((level+1)/M)
        dx = int((level+1)%M)
        
        if dy-1 >= 0 :
            if color_map[dy-1][dx] == color:
                continue
        
        # 왼쪽 확인
        if dx-1 >= 0:
            if color_map[dy][dx-1] == color:
                continue
        
        cnt += dfs(level+1, color)
    
    color_map[y][x] = 0
    return cnt
    
N, M = map(int, input().split())  # 행, 렬

color_map = [[0]*M for _ in range(N)]
color_set = set()
dir = [[-1,0], [0,-1]]  # 위와 옆만 보면 된다

# print(color_map)

ans = dfs(0, 1)  # 하나의 경우만 구하면 나머지는 *3
ans *= 3
print(ans)