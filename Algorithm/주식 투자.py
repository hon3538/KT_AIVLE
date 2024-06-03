'''
N일이 지났을 때, K원이 되는 경우의 수
하루에 +100 또는 -100의 변동

N <= 10

dfs 로 접근하면 2^10이면 되는거 아닌가..?
'''

def dfs(level, price):
    global K, N
    if level == N:
       if price == K:
           return 1
       return 0 
        
    return dfs(level + 1, price - 100) + dfs(level + 1, price + 100) 


N, K = map(int, input().split())  # N일, K 원

ans = dfs(0, 0)
print(ans)