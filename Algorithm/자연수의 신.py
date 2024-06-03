'''
N개 자연수 배열,
홀수 오름차순 + 짝수 오름차순 순서대로 배열

K 번째 자연수는?

N<=10^12

[설계]
N/2+N%2 -> 홀수 개수
N/2 -> 짝수 개수 

K번째


홀수 개수보다 크면,
K = (K-홀수 개수)*2

작으면
K = K*2 -1
'''
N, K = map(int, input().split())

odd_cnt = int(N/2) + N%2
even_cnt = int(N/2)

ans = 0
if K > odd_cnt:
    ans = (K-odd_cnt)*2
else:
    ans = 2*K - 1

print(ans) 