'''
맨 뒤에 연속하는 0을 Trailing zero라고 한다.
p 진법과 N이 주어질 때,
N! 의 p진법에서의 Trailing Zero 개수를 구하라

[설계]
10진법의 경우 0을 만드는 조건이 2x5 이다. 즉 소인수 분해하여 2와 5의 한 쌍이 숫자 0을 만든다.
8진법은 2x2x2 가 0을 만든다
7진법은 7이 0을 만든다.

소인수분해하여 소수의 개수를 통해 0의 개수를 구할 수 있다.

곱해지는 수가 1000이하이므로
1000까지 표현할 수 있는 소수 리스트를 구하면 된다. 
에라토스테네스의 체를 사용하여 1000이하의 소수를 구해준다.

'''

def getPrimeList(n):  # n 이하의 소수 리스트 return
    prime_check = [False] * (n+1)
    
    for i in range(2, int(n**0.5) + 1):  # 루트 1000까지만 보면 1000까지의 소수를 구할 수 있음
       if prime_check[i] == True:
           continue 
       
       cur = 2*i  # 소수 본인 제외 배수들만 True로 체크
       while cur <= n:
           prime_check[cur] = True
           cur += i
           
    prime_list = []
    for i in range(2, n+1):
        if not prime_check[i]:  # False 들이 소수이다.
            prime_list.append(i)
    
    return prime_list


def countPrime(num, prime_cnt):  # num의 소인수 분해 결과를 prime_cnt 에 저장
    global prime_list
    
    for p in prime_list:    
        while num%p == 0:
            prime_cnt[p] += 1
            num /= p

    
def countZeros(p, n):  # p진법 n!
    global prime_cnt
    
    for i in range(1, n+1):  # 팩토리얼
        countPrime(i, prime_cnt)
    

    # p의 소인수 분해
    p_prime_cnt = [0]*(n+1)
    countPrime(p, p_prime_cnt)
    
    # p의 소수 set가 팩토리얼에서 몇 개 포함되어 있는지 확인
    min_cnt = 0x7fffffff # 각 p의 prime별로 팩토리얼 prime 결과에 몇 번 포함되어 있는지 확인
    for i in range(1, n+1):
        if p_prime_cnt[i] == 0:
            continue 
        
        cnt = int(prime_cnt[i] / p_prime_cnt[i])  # 만약 팩토리얼 소인수 분해 결과 2가 6개, 5가 10개이고, p는 2가 5개, 5가 2개 있다면 총 1개의 0을 포함한다.
        min_cnt = min(min_cnt, cnt)
    
    if min_cnt == 0x7fffffff:  # 아예 없는 경우
        return 0
    
    return min_cnt


    
p, n = map(int, input().split())  # p-진법, n!
prime_list = getPrimeList(n)
prime_cnt = [0]*(n+1)

ans = countZeros(p, n)
print(ans)