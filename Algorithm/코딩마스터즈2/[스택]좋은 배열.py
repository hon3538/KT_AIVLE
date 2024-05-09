'''
배열 a에 1부터 N까지의 양의 정수가 각각 2개씩 포함되어 있습니다. 
즉, 배열 a의 길이는 2N입니다.

a의 i번째 원소를 a_i라고 할 때, 다음 조건을 만족하는 a를 “좋은 배열”이라고 정의합니다.

- 모든 정수 i, j, p, q (1 ≤ i < j < p < q ≤ 2N)에 대해 a_i = a_p이면 a_j ≠ a_q이다.

배열 a가 주어질 때, 배열 a가 좋은 배열인지 아닌지 판단하는 프로그램을 작성하세요.

[입력]
첫째 줄에 양의 정수 N이 주어집니다. (2 ≤ N ≤ 1,000)
둘째 줄에 2N개의 양의 정수 a_1, a_2, …, a_2N이 공백으로 구분되어 주어집니다. (1 ≤ a_i ≤ N)

[출력]
좋은 배열이면 “YES”, 좋은 배열이 아니면 “NO”를 출력합니다. (큰 따옴표 제외)
'''
'''
[설계]
모든 정수가 두 번씩 들어있고, 두 개의 A 정수 사이에 있는 정수 B는 오른쪽 A보다 뒤쪽에 존재하면 안 된다. 
즉, 두 개의 정수 사이에 한 쌍이 모두 들어있던가, 아예 없어야 한다.

stack 이용해서 비어있거나 top과 다르면 add하고
top과 같으면 pop

한 번 스택에 넣은 숫자들은 set에 저장해두는데, 두 번째 나온 숫자가 top과 다르다면 문제 있는 것이다.
'''

N = int(input())
num_list = list(map(int, input().split()))
ans = 'YES'

stack = []
used = set()

for num in num_list:
    if len(stack) == 0:
        stack.append(num)
        used.add(num)
        continue

    if not num in used:  # stack에 들어간 적 없으면
        stack.append(num) 
        used.add(num)
        continue

    if stack.pop() != num:
        ans = 'NO'
        break

print(ans)




