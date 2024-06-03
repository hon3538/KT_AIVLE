'''
- 이전에 위치한 기둥의 번호보다 더 큰 번호의 기둥으로 점프해야 합니다.
- 이전에 위치한 기둥보다 더 높은 기둥으로 점프해야 합니다.
- 더이상 점프할 수 없어지면 놀이가 종료됩니다.

단, 놀이를 시작하는 시점에 F는 땅에 위치합니다. 
땅에서는 어떤 기둥으로든 점프할 수 있지만, 
기둥에서 땅으로 점프하는 것은 불가능합니다.

[입력]
첫째 줄에 기둥의 개수 N이 주어집니다. (1 ≤ N ≤ 1,000)
둘째 줄에 i번 기둥의 높이 H_i가 공백으로 구분되어 주어집니다. (1 ≤ H_i ≤ 10,000)

[출력]
첫째 줄에 개구리가 할 수 있는 점프의 최대 횟수를 출력합니다.

[설계]
맨 왼쪽부터 시작점을 하나씩 옮겨가면서 뛸 수 있는 기둥의 수를 counting 한다
-> 실패
1 4 2 3 7
1 에서 2로가야 이득인데, 4로 가면 손해임

오른쪽부터 탐색해서 
i번째 기둥에서 오른쪽으로 점프할 수 있는 최대 횟수를 구한다
= 오른쪽 기둥의 최대횟수 + 현재 내가 점프할 수 있는 지 여부

1000*1000 = 100만
[최적화]

'''

N = int(input())  # 기둥의 개수
pillars = list(map(float, input().split()))  

ans = 0
jumps = [0]*N
for pos in range(N-1, -1, -1):  # n-1번 -> 0번 시작 위치
    max_jump = 0
    for comp in range(N-1, pos, -1):  # n-1 -> pos + 1 
        if (pillars[pos] < pillars[comp]):
            if (max_jump < (jumps[comp] + 1)):
                max_jump = jumps[comp] + 1

    jumps[pos] = max_jump
    if (ans < jumps[pos]):
        ans = jumps[pos]     
        
print(ans + 1)  # 시작지점 jump + 1
            