'''
각 카드에 정수가 쓰여 있는 N개의 볼펜이 있습니다. 단, 같은 수가 쓰여 있는 볼펜이 여러 개 있을 수 있습니다.
N개의 볼펜에서 2개 혹은 3개의 볼펜을 선택하고, 선택한 볼펜들에 쓰여있는 수들을 곱했을 때 나올 수 있는 결과 중에서 최대값을 구하는 프로그램을 작성하세요.
예를 들어 N = 6이고, 볼펜에 쓰여 있는 수들이 5, 10, -2, 3, 5, 2라고 합시다. 이때 쓰여 있는 수가 각각 5, 10, 5인 세 개의 볼펜을 선택하면 이들의 곱은 250이고, 이것이 구하고자 하는 최대값입니다.
다른 예로 N = 4이고, 볼펜에 쓰여 있는 수들이 10, 0, -5, 2라고 합시다. 이때는 각각 10, 2가 쓰여있는 두 개의 볼펜을 선택하면 두 수의 곱은 20이고, 이것이 구하고자 하는 최대값이 됩니다.

[입력]
첫째 줄에 볼펜 개수를 나타내는 정수 N이 주어집니다. (3 ≤ N ≤ 20)
둘째 줄에 볼펜에 쓰여 있는 N개의 숫자들이 차례대로 주어집니다. 이 때 숫자는 -500보다 크거나 같고 500보다 작거나 같은 정수입니다.

[출력]
숫자 2개의 곱 혹은 3개의 곱 중에서 최대값을 첫째 줄에 출력합니다.
'''
'''
[설계]
dfs 로 전체 탐색
20C3 -> 20^3 = 8천
'''

N = int(input())
ans = -0x7fffffff
pen_list = list(map(int, input().split()))

def dfs(level, start, mul_val):
    global N, ans, pen_list

    if level == 2:  # 두 개 선택한 경우
        if ans < mul_val:
            ans = mul_val

    if level == 3:  # 세 개 선택한 경우
        if ans < mul_val:
            ans = mul_val
        return

    for i in range(start, N):
        dfs(level + 1, i+1, mul_val * pen_list[i])

dfs(0, 0, 1)
print(ans)