'''
정수 n이 주어졌을 때, 십진법 체계에서 팩토리얼의 Trailing Zero 갯수가 
n보다 작지 않게 되는 최솟값이 얼마인지 알아내는 프로그램을 작성하세요.

n <= 1000

[설계]
2x5 의 쌍 개수를 세면 0의 개수가 된다.

하나씩 값을 2와 5(소수)의 개수를 cnt해서 저장하고
한 쌍이 되면 zero cnt,
zero cnt가 n보다 크거나 같아지면 그때의 팩토리얼 값을 구한다.
'''

n = int(input())  # 최소 zero 개수

cnt_2 = 0
cnt_5 = 0
zero_cnt = 0
factorial = 1
while zero_cnt < n:
    factorial += 1
    
    temp = factorial        
    while temp%2 == 0:
        cnt_2 += 1
        temp /= 2
    
    while temp%5 == 0:
        cnt_5 += 1
        temp /= 5
    
    zeros = min(cnt_2, cnt_5)
    cnt_2 -= zeros
    cnt_5 -= zeros
    
    zero_cnt += zeros
    
print(factorial)
        

