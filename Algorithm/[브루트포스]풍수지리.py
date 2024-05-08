'''
땅은 N행 M열의 격자판으로 나눌 수 있고, 격자판의 각 칸은 A부터 Z까지 26종류의 기운 중 하나를 내뿜습니다. 
이 땅 위에 바닥이 직사각형 꼴인 건물을 지었을 때, 건물 바닥과 맞닿은 칸이 모두 같은 기운을 내뿜는다면 건물에서 하는 모든 사업이 바닥과 맞닿은 칸의 수만큼 축복받게 됩니다.
첫번째 예시 입력을 봅시다. 2행 1열을 왼쪽 위 꼭짓점, 3행 3열을 오른쪽 아래 꼭짓점으로 하는 영역에 건물을 지으면 B 기운으로부터 6 만큼의 축복을 받을 수 있습니다. 
하지만 1행 3열을 왼쪽 위 꼭짓점, 2행 4열을 오른쪽 아래 꼭짓점으로 하는 영역에 건물을 지으면 여러가지 기운이 섞여 있어 축복을 받을 수 없습니다.
이 놀라운 사실을 깨달은 기성은 어서 땅을 사려고 합니다. 
격자판으로 나눈 땅의 각 칸이 어떤 기운을 내뿜는지 주어지면, 최대 얼마만큼의 축복을 받을 수 있는지 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 두 정수 N과 M이 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 8, 1 ≤ M ≤ 8)
다음 N개의 줄에 걸쳐 각 줄에 M개의 문자가 주어집니다.
격자판 i행 j열의 칸은 i + 1번째 줄의 j번째 문자와 같은 기운을 내뿜습니다.

[출력]
주어진 땅에서 최대 얼마만큼의 축복을 받을 수 있는지 출력합니다.
'''
'''
[설계]
각기 다른 모양의 직사각형으로 8x8 행렬 탐색
64개의 직사각형 조합나올 수 있고 * 각각 64번 탐색 + a = 1만번이내
'''
def is_same(y, x, h, w):
    global ground_map
    target = ground_map[y][x]
    for i in range(y, y+h):
        for j in range(x, x+w):
            if ground_map[i][j] != target:
                return False
    
    return True

def get_point(h, w):
    global N, M

    for y in range(N):
        if (y + h) > N : 
            break

        for x in range(M):
            if (x + w) > M:
                break

            if is_same(y, x, h, w):  # 만약 모든 땅의 요소가 같다면
                return h*w
            
    return 0

N, M = map(int, input().split())  # 행, 열
ground_map = []
ans = 0

for _ in range(N):
    s = input()
    ground_map.append(s)

for h in range(N, 0, -1):  # 1~N 길이까지
    for w in range(M, 0, -1):  # 1~M 길이까지
        point = get_point(h, w)
        
        if ans < point:
            ans = point

print(ans)