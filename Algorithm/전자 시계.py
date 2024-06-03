'''
hour[0] == min[1]
hour[1] == min[0]
인 시간을 찾아야 한다.

t시각부터 K 분 단위로 시각을 확인할 때, 위 조건을 만족하는 시각의 개수 출력

[설계]
44분씩 추가하면서 
hour와 min을 보고 같은 조합이 나오기 전까지 반복해서 조건에 맞는 시각 counting
'''

h, m = map(int, input().split(':'))
k = int(input())

time = h*100 + m
time_set = set()
cnt = 0
while not time in time_set:
    time_set.add(time)

    h10, h1 = int(h/10), h%10
    m10, m1 = int(m/10), m%10
    
    if (h10 == m1) & (h1 == m10):
        cnt += 1
        
    m = (m+k)%60
    h = (h+int((m+k)/60))%24
    time = h*100 + m
print(cnt)

    
