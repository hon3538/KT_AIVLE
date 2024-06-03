'''
N번째 알람이 울리는 시각
각 알람 사이에는 N-1 분 간격

[설계]
N번째 알람 시각 = 현재 시각 + 1 + 2 + 3 + ... + N-1
등차수열 합 공식

(N-1)*(1+(N-1))/2

'''
h, m = map(int, input().split(':'))
N = int(input())

mins = (N-1)*(1+(N-1))//2

mm = (m + mins)%60
hh = (h + int((m + mins)/60))%24

str_m = str(mm)
str_h = str(hh)

if len(str_m) == 1:
    str_m = '0' + str_m

if len(str_h) == 1:
    str_h = '0' + str_h

ans = str_h + ':' + str_m
print(ans)