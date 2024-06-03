'''
1
1   1
2   1   1
3   2   1
5   3   2
8   5   3
13  8   5
21
34
55

fibo(N) = fibo(N-1) + fibo(N-2)
        = fibo(N-2)+fibo(N-3) + fibo(N-4) + fibo(N-5)

...
 



피보나치 
N 분후 두 개의 합
N이.. 1조 너무 크다.. 반복문으로 돌리면 시간 초과난다.

규칙을 찾아야할 거 같다.
'''
N = int(input())

time = 1
prev = 0
now = 
