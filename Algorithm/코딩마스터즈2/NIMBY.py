'''
수직선 위에 N개의 집이 있습니다. 
그 중 한곳을 골라 쓰레기 소각장을 지으려고 합니다. 
공공의 이익이 되는 시설이므로 가까울수록 주민의 만족도가 늘어나지만, 
너무 가까우면 오히려 만족도가 줄어듭니다. 

이를 명확하게 정의하면 다음과 같습니다. 
쓰레기 소각장과 집까지의 거리를 d라고 할 때, 
쓰레기 소각장과 거리가 K이하인 집은 d만큼의 만족도를, 
K초과인 집은 -d만큼의 만족도를 갖게 됩니다.

모든 집의 만족도의 합을 최대화 하기 위한 쓰레기장의 위치를 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ K ≤ 100,000)
이어서 다음 줄에, 수직선 위의 집의 좌표 A_i, N개가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 100,000)

[출력]
모든 집의 만족도의 합을 최대화 하기 위한 쓰레기장의 위치를 출력합니다.
만약 그런 위치가 여러개라면, 가장 좌표가 작은 곳을 출력합니다.

[설계]
100개 집에 각각 설치하는 경우 * 100개집 거리계산 = 1만
'''
N, K = map(int, input().split())  # 집 개수, 거리 제한
houses = list(map(int, input().split()))  # 각 집의 좌표
houses = sorted(houses)
satisfaction = -0x7fffffff
ans = -1
for i, house in enumerate(houses):
    # i 번째 집을 소각장으로 선택한 경우
    point = 0
    # 왼쪽으로 만족도 계산
    for l in range(i - 1, -1, -1):
        dist = house - houses[l]
        if dist <= K:
            point += dist
        else:
            point -= dist

    # 오른쪽으로 만족도 계산
    for r in range(i+1, N):
        dist = houses[r] - house
        if dist <= K:
            point += dist
        else:
            point -= dist

    if satisfaction < point:
        satisfaction = point
        ans = house
print(ans)