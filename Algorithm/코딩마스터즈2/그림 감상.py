'''
그림들 중에서도 4 × 4 크기의 O, X 문자로만 이루어진 그림만을 감상합니다.

하준은 그림을 감상할 때, 
그림에 2 × 2 크기의 X로만 이루어진 영역이 있는지를 중점적으로 봅니다. 
그런데, 하준은 딱 한 번 그림의 O 하나를 X로 바꿀 수 있는 마법의 붓을 얻었습니다.

하준은 이 붓을 최대 한 번 이용한 후 주어진 그림에 2 × 2 크기의 X로만 이루어진 영역이 있을 수 있는지 궁금해졌습니다.

[입력]
4 × 4 그림이 4줄에 걸쳐서 주어집니다.
그림은 항상 대문자 O와 대문자 X로만 이루어져 있습니다.

[출력]
하준이가 마법의 붓을 최대 한 번 이용한 후 주어진 그림에 2 × 2 크기의 X로만 이루어진 영역이 있을 수 있다면 yes, 아니면 no를 출력합니다. 답은 무조건 소문자로만 출력해야 함에 유의하세요.
'''
'''
[설계]
2x2 탐색하며 X개수가 3개 이상인 곳이 있으면 yes, 아니면 no
'''
def get_x_cnt(y, x):
    global ox_map
    x_cnt = 0
    for i in range(2):
        for j in range(2):
            if ox_map[y+i][x+j] == 'X':
                x_cnt += 1
    return x_cnt

ox_map = []
for _ in range(4):
    ox_map.append(input())

ans = 'no'
for y in range(3):
    for x in range(3):
        x_cnt = get_x_cnt(y, x)
        if x_cnt >= 3:
            ans = 'yes'
            break
    if ans == 'yes':
        break

print(ans)