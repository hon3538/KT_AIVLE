'''
전재도 종류는 11개가 있다.
각 전개도는 3x4 맵으로 표현할 수 있다.
각 전개도가 시계방향으로 돌아가 있는 경우를 확인하기 위해
4 를 곱해준다.

각 전재도 별로 10x10 = 100번을 탐색하여 비교한다.

11*3*4*4*100 = 약 5만 3천번 연산으로 해결 가능하다.

4방향으로 전개도를 돌리는 대신, 맵이 돌아가 있다고 가정하고 좌표만 치환하자

0, 0 -> 9, 0
0, 9 -> 0, 0
1, 1 -> 8, 1
y, x -> 9-x, y  

4방향으로 돌리는 것 외에도,, 대칭도 있다...
x 대칭 y 대칭 따로 봐줘야한다.
'''

def turn_block(figure):  # 반시계방향으로
    h = len(figure)
    w = len(figure[0])
    
    new_figure = [['']*h for _ in range(w)]
    for y in range(h):
        for x in range(w):
            new_figure[w-x-1][y] = figure[y][x]
    return new_figure


def flip_block(figure):  # x축 대칭으로 뒤집기
    h = len(figure)
    w = len(figure[0])
    
    new_figure = [['']*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            new_figure[y][w-1-x] = figure[y][x]
    return new_figure
            
def get_sum(y, x, figure, Map):
    h = len(figure)
    w = len(figure[0])
    cnt = 0
    for dy in range(h):
        for dx in range(w):
           if figure[dy][dx]=='1':
               cnt += int(Map[y+dy][x+dx])
    return cnt 
    
# 전개도 종류 미리 만들기
figures = [
    ['1000', '1111', '1000'],
    ['1000', '1111', '0100'],
    ['1000', '1111', '0010'],
    ['1000', '1111', '0001'],
    ['0100', '1111', '0100'],
    ['0100', '1111', '0010'],
    ['1000', '1110', '0011'],
    ['0100', '1110', '0011'],
    ['0010', '1110', '0011'],
    ['11100', '00111'],
    ['1100', '0110', '0011']
]

maps = []
for _ in range(10):
    maps.append(list(input().split()))


# Map 돌렸을 때
ans = 0  
for figure in figures:
    # 4방향 
    for i in range(4):
        figure = turn_block(figure)
        h = len(figure)
        w = len(figure[0])
        for y in range(10-h):
            for x in range(10-w):
                for i in range(4):  # 4방향 찾기
                    result = get_sum(y, x, figure, maps)
                    if ans < result:
                        ans = result
    figure = flip_block(figure)  # 대칭으로 뒤집기 
    for i in range(4):
        figure = turn_block(figure)
        h = len(figure)
        w = len(figure[0])
        for y in range(10-h):
            for x in range(10-w):
                for i in range(4):  # 4방향 찾기
                    result = get_sum(y, x, figure, maps)
                    if ans < result:
                        ans = result
            
print(ans)
