'''
길에 N개의 싱크홀이 생겼습니다.

이 싱크홀을 그대로 놔두면 위험하기 때문에, 
준하는 가지고 있는 길이가 K인 널빤지를 이용해 임시로 보수하려고 합니다. 

싱크홀의 위치와 널빤지의 길이가 주어질 때, 
싱크홀을 모두 덮기 위한 널빤지의 최소 개수를 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ K ≤ 100,000)
둘째 줄에 싱크홀의 위치 A_i가 공백으로 구분되어 주어집니다. (1 ≤ A_i ≤ 100,000)

[출력]
싱크홀을 모두 덮기 위한 널빤지의 최소 개수를 출력합니다.

[설계]
Greedy, 시작지점에 골판지 깔고 골판지 길이가 끝난 뒤에 만나는 시작지점에 다시 까는 방식으로 진행
'''
N, K = map(int,input().split())
sinkholes = list(map(int,input().split()))
sinkholes = sorted(sinkholes)

cnt = 0
pos_end = -1
for hole in sinkholes:
    if pos_end < hole:
        cnt += 1
        pos_end = hole + K - 1

print(cnt)