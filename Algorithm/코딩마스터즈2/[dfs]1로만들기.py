'''
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.

1. X가 5로 나누어 떨어지면, 5로 나눕니다.
2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
3. X가 2로 나누어 떨어지면, 2로 나눕니다.
4. X에서 1을 뺍니다.

정수 X가 주어졌을 때, 위와 같은 연산 4개를 적절히 사용해서 1을 만들려고 합니다. 연산을 사용하는 횟수의 최솟값을 출력합니다.
예를 들어 정수가 26인 경우 26 -> 25 -> 5 -> 1로 3번의 연산이 최솟값입니다.

첫째 줄에 정수 X가 주어집니다. (1 ≤ X ≤ 30,000)
첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.

전략
dfs로 전부 실행
'''
min_value = 0xffffffff
def dfs(level, x):
    global min_value

    if x == 1:  # 1이면 나가
        min_value = min(min_value, level)
        return
    
    if level >= min_value:  # 현재 연산 횟수가 최소보다 같거나 크다면 나가, backtracking
        return
    
    if x % 5 == 0:
        dfs(level + 1, x/5)
    26
    if x % 3 == 0:
        dfs(level + 1, x/3)

    if x % 2 == 0:
        dfs(level + 1, x/2)

    dfs(level + 1, x-1)
    

min_value = 0xffffffff

x = int(input())

dfs(0, x)

print(min_value)