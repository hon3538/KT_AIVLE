'''
치훈은 생일 선물로 배열 A를 받았습니다.

배열 A의 서로 다른 네 인덱스 i, j, k, l에 대하여,
A_i * A_j = A_k * A_l를 만족하는 i, j, k, l가 존재하는지 출력하는 프로그램을 작성하세요.

A_i는 배열 A의 i번째 원소를 뜻합니다.

[입력]
첫 줄에 N이 주어집니다. (4 ≤ N ≤ 50)
두번째 줄에 길이 N의 배열 A가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 1000)

[출력]
존재하면 YES, 아니면 NO를 출력합니다.
'''
'''
[설계]
50C4 로 4개 뽑고 4개를 조합하면 4가지 경우가 있음

즉, 150만 * 3 = 450 만번 연산
'''
def is_possible(s):
    global num_arr
    if num_arr[s[0]]*num_arr[s[1]] == num_arr[s[2]]*num_arr[s[3]]:
        return True
    if num_arr[s[0]]*num_arr[s[3]] == num_arr[s[1]]*num_arr[s[2]]:
        return True
    if num_arr[s[0]]*num_arr[s[2]] == num_arr[s[1]]*num_arr[s[3]]:
        return True
    return False

def dfs(level, start_index, selected):
    global N
    if level == 4:
        # 조합
        if is_possible(selected):
            return True
        return False

    for i in range(start_index, N):
        selected.append(i)
        flag = dfs(level+1, i+1, selected)
        selected.pop()

        if flag:
            return True



N = int(input())
num_arr = list(map(int, input().split()))

result = dfs(0, 0, [])
if result :
    print('YES')
else:
    print('NO')
