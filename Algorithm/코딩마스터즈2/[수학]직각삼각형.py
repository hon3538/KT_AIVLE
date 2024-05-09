'''
직각삼각형의 둘레가 120일 때, 세 변의 길이가 모두 양의 정수인 직각삼각형은 다음과 같이 3가지입니다.
(20, 48, 52), (24, 45, 51), (30, 40, 50)

1 이상 N 이하의 둘레 중에서, 세 변의 길이가 모두 양의 정수인 직각삼각형을 가장 많이 만들 수 있는 둘레와 그때 만들어지는 직각삼각형의 개수를 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 양의 정수 N이 주어집니다. (12 ≤ N ≤ 2,400)
단, 세 변의 길이가 모두 양의 정수인 직각삼각형을 최소 1개 이상 만들 수 있는 입력만 주어집니다.

[출력]
첫째 줄에 정답을 출력합니다.
단, 조건을 만족하는 둘레가 여러 개인 경우 그 중에서 가장 작은 둘레를 출력합니다.
'''
'''
[설계]
3~2400 둘레 중에서
피타고라스 정리 a^2 + b^2 = c^2 ( a, b < c )를 만족하는 삼각형 개수 찾기

a + b + c = 둘레 ( a, b < c )

a, b 길이를 바꿔가며 c를 찾고 그 때의 둘레 길이가 나온 횟수를 indexing 배열을 활용하여 counting 한다

'''

N = int(input())
cnt_arr = [0]*(N+1)

ans_cnt = 0  # max_cnt
ans_len = 0  # min_len

for a in range(1, int(N/2)):
    for b in range(a+1, int(N/2)):  # b가 항상 a보다 같거나 크다
        c = (a**2 + b**2)**0.5
        len = a + b + c 
        if len > N:  # 세 길이의 합이 둘레 범위를 넘은 경우
            break

        if int(c) <= b | int(c) <= a:  
            break
        
        if (c - int(c)) == 0:  # c가 정수
            cnt_arr[int(len)] += 1

for i, cnt in enumerate(cnt_arr):
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans_len = i

print(ans_len, ans_cnt)
