'''
최대 점수 순서대로 정렬 필요
2000*2000 = 400만 -> 점수들 계산

각 점수들은 
i~j 번째 값들의 곱에서 M의 나머지이다.
하지만 각 요소 값들이 최대 100만인데, 1~2000 번째 요소까지 모두 곱하면
숫자가 너무 커지게 된다. 오버플로우 발생..

각각의 값을 M으로 나눈 나머지끼리 곱셈을 하면, 
기존 값의 곱셈 연산결과에 M으로 나눈 나머지의 결과와 같은가?
ex) M == 6 인경우
7*8%6 과 (7%6) * (8%6)은 같은가..? 아니라면 나머지연산은 분배법칙이 적용 안 되나>
2 와 1*2 로 같다..?
8*10%6 과 ((8%6) * (10%6))%6
2와 2..로 같다
마지막, M=7인경우
8*9%7 , 8%7 * 9%7
2 , 1*2 로 같다!


정렬 400만 ( log400만) = 8000만..? 이게 돼?
해보자

각 순간에 최대가 되는 점수를 찾는 건 맞아


'''
N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
    
cal_list = []  # 모든 i~j 조합에 대한 곱셈 값을 M으로 나눈 나머지로 저장
for i in range(N):  # 0~N-1
    prefix = 1
    for j in range(i, N):  # i~j 까지 곱 
        result = (prefix*num_list[j])%M 
        cal_list.append(result)
        prefix = result
        
cal_list = sorted(cal_list, key = lambda x : -x)
ans = 0
for i in range(len(cal_list)):
    if i%2 == 0:
        ans += cal_list[i]
    else:
        ans -= cal_list[i]
print(ans)