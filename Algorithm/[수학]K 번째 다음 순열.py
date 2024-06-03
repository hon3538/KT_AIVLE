'''
1부터 N까지의 자연수로 이루어진 순열이 있습니다. 
이 순열의 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 
가장 마지막에 오는 순열은 내림차순으로 이루어진 순열입니다.

예를 들어 N이 3인 경우 사전 순으로 나열하면 다음과 같습니다.

1 2 3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

이때 순열 (2 3 1)의 사전 순으로 다음 순열은 (3 1 2) 입니다.
또한 순열 (2 3 1)의 사전 순으로 2번째 다음 순열은 (3 2 1)입니다.

대희는 "대희식 순서"를 만들었습니다. 
"대희식 순서"란 사전식 순서를 따르면서 다음 규칙 하나를 추가한 것입니다.

사전 순으로 가장 마지막 순열의 다음 순열은 사전 순으로 가장 앞서는 순열이다.

예를 들어 N이 3인 경우
순열 (3 1 2)의 대희식으로 다음 순열은 (3 2 1) 입니다.
순열 (3 1 2)의 대희식으로 2번째 다음 순열은 (1 2 3)입니다.

어떤 순열이 주어질 때 대희식으로 K번째 다음 순열을 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 자연수 N과 K가 공백으로 구분되어 주어집니다.(2 ≤ N, K ≤ 1,000)
둘째 줄에 순열이 공백으로 구분되어 주어집니다.

[출력]
어떤 순열이 주어질 때 대희식으로 K번째 다음 순열을 공백으로 구분하여 출력합니다.

[설계]
조합은 N! 앞에서부터 숫자를 비교하여 경우를 더해가면서 몇 번째 수열인지 구한다.
그리고 그 수열에 K를 더하여 해당 수열을 구한다.
'''
def getCnt(num):  # num보다 작은 나올 수 있는 값들 개수
    global used
    cnt = 0
    for i in used[1:num]:
        if not i:
            cnt += 1
    return cnt

def getNum(order):  # 가능한 수들 중에서 order 번째 값 return
    global used
    cnt = 0
    for i in range(len(used)):
        if not used[i+1]:
            cnt += 1
        if cnt == order:
            return i+1
        
    
N, K = map(int, input().split())  # N개 자연수, K 번째 다음 순열
current = list(map(int, input().split()))  # 현재 순열
origin = sorted(current)  # 원래 순열

N_factorial = 1
for i in range(1, N+1):  # N! 미리 계산
    N_factorial*=i

factorial = N_factorial
order = 0
used = [False]*(N+1)  # index : 숫자, value : 등장 여부
for i in range(N):
    factorial //= (N-i)  # i번째 이후 값들에 대한 factorial
    cnt = getCnt(current[i])
    used[current[i]] = True
    
    order += (cnt*factorial)

# K 번째 수열은 (order + K)%N_factorial
target_order = (order + K)%(N_factorial)  # 0부터

factorial = N_factorial 
used = [False]*(N+1)  # index : 숫자, value : 등장 여부

ans_list = []
for i in range(N):
    factorial //= (N-i)
    order = int(target_order//factorial) + 1

    target_order = target_order%factorial
    num = getNum(order)
    used[num] = True
    
    ans_list.append(num)

for ans in ans_list:
    print(ans, end=' ')

# K <= 1000 이라서 1000번째 순열을 찾는 문제라서
# 더 효율적인 방법이 없을까..?
# 들어온 순열 그 상태에서 바로 K번째 순열을 찾는 방법을 고민해보자..