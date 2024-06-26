'''
조선시대의 거상 한울은 거대한 이무기가 자신의 재산을 약탈하러 온다는 이야기를 들었습니다. 
그래서 자신이 가지고 있는 재산을 지키기 위해 여러 명의 용병을 고용했습니다. 
각 용병은 제각각 자신만의 전투력을 가지고 있습니다. 

한울은 전투에 대비하기 위해 자신의 용병들이 가지는 전력을 파악하고자 합니다. 
용병들은 서로 전투력이 동화되는 성격을 가지고 있어서, 
여러 명의 용병들이 있을 때에는 가장 전투력이 낮은 용병과 동일하게 나머지 용병들의 전투력이 조정됩니다.
따라서 한울은 가장 전투력이 높은 용병부터 팀에 넣으며 전투력이 최대가 되게 하려 합니다.

예를 들어 용병이 4명이고, 
각 용병의 전투력이 (43, 50, 80, 23)이라면 최대 전투력의 합은 (43, 50, 80)을 선택한 것으로 43 * 3 = 129입니다.

한울을 위해 모든 용병들의 전투력이 주어졌을 때, 용병들의 전투력의 합이 최대가 얼마인지 구하는 프로그램을 작성하세요.

[입력]
첫째 줄에 용병의 수 N이 주어집니다. (1 ≤ N ≤ 10,000)
둘째 줄에는 각 용병들의 전투력 K가 공백을 기준으로 주어집니다. (1 ≤ K ≤ 10,000)

[출력]
첫째 줄에 문제에서 요구하는 정답을 출력합니다.
'''
N = int(input())

s_list = map(int, input().split())

s_list = sorted(s_list, reverse=True)

ans = 0
for i, s in enumerate(s_list):
    if ans <= s*(i+1):
        ans = s*(i+1)

print(ans)