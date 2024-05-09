'''
그래서 알람을 맞춰 놓아도 바로 일어나지 못해서 알람이 여러번 울리도록 설정해 놓았습니다. 

처음 알람이 울린 다음, 두 번째 알람은 1분 후, 세 번째 알람은 두 번째 알람이 울린 다음 2분후, ..., 
K번째 알람은 K-1번째 알람이 울린 다음 K-1분 후에 울립니다.

준하가 알람을 맞춘 시각이 주어질 때,
N번째 알람이 울리는 시각을 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 알람을 맞춘 시각이 "HH:MM"형태로 주어집니다.
둘째 줄에 N이 주어집니다. (1 ≤ N ≤ 1,000,000,000)

[출력]
N번째 알람이 울리는 시각을 "HH:MM"형태로 출력합니다.
HH는 00, 01, 02, ..., 23 중에 하나이며, MM은 00, 01, 02, ..., 59 중 하나입니다.

[설계]
N이 10억이기 때문에 완전 탐색은 불가능 -> 수학식 계산 필요

1 + 2 + 3 .. + (K-1)

(K-1)(1 + (K-1)) / 2 -> 등차수열 합 공식 활용
-> 왜 안 되지..? 10억이 들어올 경우 데이터형에 문제가 있나?

'''

H, M = map(int, input().split(':'))
N = int(input())

# mins = int((N-1)*(1+(N-1))/2)  # 추가 min
# hours = int((mins+M)/60)  # 추가 hour

temp = (N-1)*(1+(N-1))
mins = H*60 + M + int(temp/2)

M = mins%60
H = int(mins/60)%24

m_str = str(M)
if len(m_str) == 1:
    m_str = '0'+str(M)

h_str = str(H)
if len(h_str) == 1:
    h_str = '0'+str(H)

print(f'{h_str}:{m_str}')