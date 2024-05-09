'''
모든 종류의 선물에 대해 개수를 공평하게 나눠줘야 합니다.
철수는 선물을 남기지 않고 최대한 많은 아이들에게 나눠주려고 합니다.
선물을 받게 되는 아이들의 최대 명수를 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 양의 정수 N이 주어집니다. (1 ≤ N ≤ 100)
둘째 줄에 양의 정수 a_i가 공백으로 구분되어 주어집니다. (1 ≤ a_i ≤ 10,000)

[출력]
첫째 줄에 선물을 받게 되는 아이들의 최대 명수를 출력합니다.
'''
'''
[전략]
가장 낮은 선물의 개수가 선물을 받게될 아이들의 최대 인원 -> X
만약 2 2 3 이라고하면 2명한테 나눠주면, 선물이 남음 1명이 최대임

parametric search -> 선물을 남기지 않는 최대 인원 -> x
가능 / 불가능의 경계면이 확인한 경우만 사용할 수 있다
3 9 6 인 경우
5명은 안돼, 2명도 안 돼, 1명은 돼 -> 1명 1?
더 최대 인원인 3명도 되는데 답은 1명으로 나와버린다.

따라서 각각의 최대 가능 인원수부터 시작해서 모든 선물의 개수를 딱 떨어지게 나눌 수 있는지 완전 탐색하는 방법이 있다
100*10000 = 100만이다.
가지고 있는 선물 개수의 최대값을 이용하면 더 줄일 수도 있겠다
'''
# def is_possible(mid):
#     global gift_cnt

#     for cnt in gift_cnt:
#         if cnt%mid != 0:
#             return False

#     return True

# def ps(left, right):
#     ans = 1
#     while left <= right:
#         mid = int((left+right)/2)
#         if is_possible(mid):
#             left = mid + 1
#             ans = mid
#         else:
#             right = mid - 1
#     return ans

# result = ps(1, 10000)  # 선물의 개수가 1만개까지이므로 이론상 1만 명이 나눌 수 있다.

N = int(input())

gift_cnt = list(map(int, input().split()))
max_cnt = max(gift_cnt)

ans = 1
for i in range(max_cnt, 0, -1):
    flag = True
    for cnt in gift_cnt:
        if cnt % i != 0:
            flag = False
            break
    if flag:
        ans = i
        break

print(ans)


    