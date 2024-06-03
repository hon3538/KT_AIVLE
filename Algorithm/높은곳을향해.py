'''
이전에 위치한 기둥보다 더 큰 번호 기둥으로 점프
이전에 위치한 기둥보다 더 높은 기둥으로 점프

왼쪽에서 오른쪽으로 점프해야된다는 기준이없잖아?
아 더 큰 번호가 오른쪽이란 의미인가..

dp[i] = i번쨰까지 최대 점프 횟수
dp[i] = max(dp[i-1])

'''
N = int(input())
pillars = list(map(int, input().split()))  # 기둥들의 높이
dp = [1]*(N+1)  # i번째까지 최대 점프 횟수


for i in range(1, N):
        for j in range(i):
            if pillars[j] < pillars[i]:  # 이전 기둥보다 높이가 큰 경우
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))