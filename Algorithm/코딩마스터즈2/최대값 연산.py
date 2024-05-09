'''
영희가 만들어낸 x, y, z는 다음과 같습니다. 
영희는 이 연산 과정을 최댓값 연산이라는 이름을 붙였습니다.

x = max(a, b), y = max(b, c), z = max(c, a)

영희는 그러던 중, a, b, c 3개의 수를 잊어버렸습니다.
뿐만 아니라, 가지고 있는 x, y, z 3개의 수가 a, b, c로부터 만들어진 수인지조차 불분명하다는 것을 인지하였습니다.

영희는 먼저 이 x, y, z라는 수가 임의의 3 수에 최댓값 연산을 해서 나올 수 있는 수인지부터 알아내려고 합니다.
3개의 양의 정수 x, y, z가 주어졌을 때, 이 3개의 수가 최댓값 연산을 해서 나올 수 있는 수인지 알아내는 프로그램을 작성하세요.

[입력]
3개의 정수 x, y, z가 공백으로 구분되어 주어집니다. (1 ≤ x ≤ y ≤ z ≤ 1,000)

[출력]
이 3개의 수가 최댓값 연산을 해서 나올 수 있는 수이면 possible, 아니면 impossible을 출력합니다. 답은 무조건 소문자로만 출력해야 함에 유의하세요.
'''
'''
[설계]
x == y 이면 b가 최대값
y == z 이면 c가 최대값
x == z 이면 a가 최대값

최대 값이 2 개 있고, 나머지 값이 더 작아야 한다.
'''
x, y, z = map(int, input().split())

max_val = max(x, y)
max_val = max(max_val, z)

cnt = 0
if max_val == x:
    cnt += 1
if max_val == y:
    cnt += 1
if max_val == z:
    cnt += 1
    
if cnt >= 2:
    print('possible')
else:
    print('impossible')