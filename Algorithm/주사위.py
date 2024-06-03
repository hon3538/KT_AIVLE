'''
1 -> 1
2 -> 2
3 -> 4
4 -> 8
5 -> 15
6 -> 29

주사위 수는 1~4 까지 있기 때문에 1~4 와 5~ 의 규칙은 다르다.
1~4는 2배
5~ 는 2배 -1 의 규칙을 따른다.

2*i-1
2*(2*i-1)-1
2*(2*(2*i-1)-1) -1
= 2^(n-4)*i -(1+2+2^2+..+2^(n-4)) 
'''
squared = [0]*50
num_map = {0:1, 1:2}
def getSquare(N): # N <= 1조
    global squared
    if N in num_map:
        return num_map[N]
    num_map[N] = getSquare(int(N/2))*getSquare(N-int(N/2))%1000000007 
    # 분할 정복으로 N값 구하기
    return num_map[N]

N = int(input())

if N <= 4:
    print(2**(N-1))
else:
    ans = getSquare(N-4)*8 -(getSquare(N-4)-1)  # 분할 정복 필요요
    print(ans%1000000007)
    # print(getSquare(N))