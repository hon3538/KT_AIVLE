'''
어느 날 기승이 종이 한장과 주사위 3개를 가져와 기성에게 게임을 제안했습니다. 
주사위는 우리가 일반적으로 알고있는 각 면에 1 이상 6 이하의 서로 다른 정수가 적힌 정육면체입니다. 
주사위를 굴리면 1 이상 6 이하의 정수를 각각 1/6의 동일한 확률로 얻을 수 있습니다. 
종이에는 N개의 수가 일렬로 적혀있으며, 모든 수는 -100 이상 100 이하의 정수입니다.

기성은 정수 K를 하나 고른 뒤 주사위 3개를 굴립니다. 
세 주사위의 눈의 합을 T라고 할 때, 기성의 점수는 종이에 K + T번째로 적힌 수와 같습니다. 
만약 K + T가 N보다 크다면 기성의 점수는 -100점입니다. 
(단, K의 범위는 1 ≤ K ≤ N 입니다.)

기승도 위와 똑같은 시행을 하여 점수가 높은 사람이 게임에서 이깁니다. 
승부욕이 발동한 기성은 어떤 K를 골라야 점수의 기댓값이 최대가 되는지 구하려고 합니다.

기성을 위해 어떤 K를 골라야 점수의 기댓값이 최대가 되는지 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 N이 주어집니다. (1 ≤ N ≤ 10,000)
둘째 줄에 종이에 적힌 N개의 정수가 공백으로 구분되어 주어집니다. (-100 ≤ 종이에 적힌 수 ≤ 100)
i번째 수는 종이에 i번째로 적힌 수와 같습니다.

[출력]
첫째 줄에 점수의 최대 기댓값에 216을 곱해 출력합니다.
기댓값에 216을 곱하면 정수가 됨을 증명할 수 있습니다.
둘째 줄에 점수의 최대 기댓값을 얻기 위해 고를 수 있는 K를 오름차순으로 모두 출력합니다.

[설계]
기대값 = 나올 확률 * 값

주사위를 던져 나올 수 있는 숫자의 경우를 각각 counting
3~18 의 숫자가 나올 수 있음 16개
각 숫자별로 K를 다르게 했을 때 기대값을 계산하여 최대값을 구하기 -> 1만 * 16
'''
def dfs(level, sum):
    global score_cnt
    if level == 3:
        score_cnt[sum] += 1
        return
    
    for i in range(1, 7):
        sum += i
        dfs(level + 1, sum)
        sum -= i

N = int(input())
num_list = list(map(int, input().split()))


score_cnt = [0]*20
dfs(0, 0)

max_val = -0x7fffffff
ans_list = []

for k in range(1, N+1):  
    total = 0
    for t in range(3, 19):  # 3 ~ 18 까지 나온 경우의 수
        score = 0
        if (k+t) > N :
            score = -100
        else:
            score = num_list[k+t-1]
            
        # 기대값 합
        total += (score * score_cnt[t])
        
    if max_val == total:
        ans_list.append(k)
        
    if max_val < total:
        max_val = total
        ans_list.clear()
        ans_list.append(k)

ans_list = sorted(ans_list)
print(max_val)
for ans in ans_list:
    print(ans, end=' ')
