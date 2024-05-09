'''
부분 행렬이란 주어진 행렬의 일부 열과 일부 행을 지워서 만들어 낸 더 작은 행렬을 말합니다. 
정수로만 이루어진 행렬과 정수 X가 주어졌을 때, 
성분의 합이 X와 같은 부분행렬이 존재하는지 알아내는 프로그램을 작성하세요.

[입력]
첫째 줄에 행렬의 크기 행과 열의 개수를 나타내는 N, M과 X가 공백으로 구분되어 주어집니다. (1 ≤ N, M ≤ 4, -1000 ≤ X ≤ 1000)
둘째 줄부터 N줄에 걸쳐, 행렬이 주어집니다. 행렬의 각 원소는 절대값이 1000이하인 정수입니다.

[출력]
성분의 합이 X와 같은 부분행렬이 존재하면 YES, 그렇지 않으면 NO를 출력합니다.
'''
'''
[설계]
부분행렬은 1x1 부터 4x4까지 될 수 있나..?
최대 4x4 행렬이니까 완전탐색
'''
def get_sum(w, h, y, x):
    global num_map
    sum = 0
    for i in range(h):
        for j in range(w):
            sum += num_map[y+i][x+j]
    return sum

def is_possible(w, h):
    global N, M, X
    for y in range(N - h + 1):
        for x in range(M - w + 1):
            result = get_sum(w, h, y, x)
            if result == X:
                return True
    return False


N, M, X = map(int, input().split())

num_map = []
for y in range(N):
    x_list = list(map(int, input().split()))
    num_map.append(x_list)

ans = 'NO'
for h in range(1, N+1):
    for w in range(1, M+1):
        if is_possible(w, h):
            ans = 'YES'
            break
    if ans =='YES':
        break
print(ans)


