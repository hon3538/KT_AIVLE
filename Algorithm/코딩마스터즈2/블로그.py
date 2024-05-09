'''
광고를 달기 위해서는 블로그의 방문자 수가 많을 수록 유리합니다. 
블로그의 관리자 메뉴에는 N일간의 방문자의 수가 기록되어 있는데, 
준하는 이 기록중 연속된 K일만 빼고 모두 삭제해서 평균 방문자가 더 많은 것처럼 만드려고 합니다. 

가장 많은 평균 방문자가 표시되도록 하기 위해서는 
몇 번째 날 부터 K일만 남겨야 하는지 계산하는 프로그램을 작성하세요.

[입력]
첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 5,000, 1 ≤ K ≤ N)
둘째 줄에 i일째의 방문자 수를 나타내는 A_i가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 1,000)

[출력]
가장 많은 평균 방문자가 표시되도록 하기 위해서는 몇 번째 날 부터 K일만 남겨야 하는지 출력합니다.
그런 날이 여러 개라면, 가장 빠른 날을 출력합니다.

[설계]
1~5000번째 날짜부터 탐색, 
5000*5000 = 25000000 이천오백만

K 탐색을 sliding window로 하면
5000번 + 5000번 만에 가능
'''

N, K = map(int, input().split())
visitors = list(map(int, input().split()))

visitors_sum = 0
for i in range(K):  # 처음 0~K-1 까지 방문자 합을 미리 구해놓는다.
    visitors_sum += visitors[i]

ans = 1  # 첫째날 
max_mean = visitors_sum / K
for head in range(0, N-K):  # head는 Sliding Window에서 빠질 앞부분
    tail = head + K
    visitors_sum = visitors_sum - visitors[head] + visitors[tail]
    mean_val = visitors_sum / K
    
    if max_mean < mean_val:
        max_mean = mean_val
        ans = head + 2

print(ans)
    



