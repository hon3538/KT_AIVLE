'''
물건 공급가격에 10% 중 소수점을 버린 수가 부가세이다.

물건 총액가가 주어질 때, 공급가와 부가가치세를 출력하라

구할 수 없는 경우는 -1 출력

[설계]
10:1 로 이루어져 있다.

만약 공급가로부터 원가를 구했을 때 소수점이 있다면, +1을 해준다.
왜냐하면, 부가가치세에 소수점이 있었을 경우 이를 버림으로써 
원가 + 부가가치세를 10:1 로 나누면 원가의 값도 일부 잃기 때문이다.

공급액을 10으로 나누어 검산했을 때, 세금과 동일하다면 가능
아니면 불가능이다.


'''
price = int(input())  # 총액가
unit = price / 11
origin = unit*10
if origin - int(origin) != 0:
    origin = int(origin) + 1
tax = int(unit)


if int(origin/10) == tax:
    print(origin, tax)
else:
    print(-1)


