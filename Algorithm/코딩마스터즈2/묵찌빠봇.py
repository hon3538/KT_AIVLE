'''
묵찌빠
1 가위
2 바위
3 보

[입력]
첫 번째 줄에 각각의 리스트의 길이를 의미하는 자연수 N, M이 공백으로 구분되어 주어집니다.
두 번째 줄에 첫 번째 묵찌빠봇에 들어갈 N개의 자연수가 공백으로 구분되어 주어집니다.
세 번째 줄에 두 번째 묵찌빠봇에 들어갈 M개의 자연수가 공백으로 구분되어 주어집니다.
(1 ≤ N, M ≤ 50)

[출력]
첫 번째 줄에 첫 번째 묵찌빠봇이 이기면 1을, 두 번째 묵찌빠봇이 이기면 2를, 영원히 승부를 계속하게 된다면 0을 출력합니다.
'''
'''
[설계]
묵찌빠룰 대로 무한루프
선공 후공 정하기
묵찌빠 시작

시작할 때 위치와 동일해진다면 영원히 반복하는 형태
'''

N, M = map(int, input().split())  # 묵찌빠 봇1, 묵찌빠 봇2 가 내는 순서

machine1 = list(map(int, input().split()))
machine2 = list(map(int, input().split()))
order1 = 0  # machine1 리스트 index
order2 = 0  # machine2 리스트 index

attack = 0
start_cnt = 0
while True:
    m1 = machine1[order1]
    m2 = machine2[order2]

    if m1 == m2 :  # 비긴 경우
        if attack != 0:  # 선공이 있다면 선공이 승리!
            break
    elif ((m1+1)%4 + int((m1+1)/4)) == m2:  # m2가 이긴 경우, m1의 다음 순서를 m2가 가지고 있으면 m2가 이김, m1 = 3 일경우 m2 = 1로 만들어주기 위한 식
        attack = 2
    else :  # m1이 이긴 경우
        attack = 1

    if order1 + order2 == 0:  # 시작 지점 cnt
        start_cnt += 1

        if start_cnt == 2:  # 한바퀴 돌았는데 승부를 내지 못하면 영원히 승부 못냄
            attack = 0
            break

    order1 = (order1+1)%N
    order2 = (order2+1)%M

print(attack)