'''
1 · 8 · 15 · 22 · 29는 일요일이므로 빨간색으로 표기합니다. 7 · 11은 주문자가 공휴일로 지정해달라고 요구했으므로 역시 빨간색으로 표기합니다. 
14 · 21 · 28은 공휴일이 아닌 토요일이므로 파란색으로 표기합니다. 나머지는 검은색으로 표기합니다. 
일요일을 제외하고, 주문자가 요구사항에 명시하지 않은 날은 우리가 익히 아는 공휴일(5월 5일 등)이라도 빨간색으로 표기해선 안 됩니다. 
날짜에 불필요한 0(leading zero)은 사용하지 않습니다. 위 달력에 대한 정답은 예시 출력을 확인해봅시다.
윤년을 제외하면 1월부터 12월까지의 말일은 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일입니다. 
주문받은 달력은 윤년이 아닌 해의 것이며, 1월 1일이 무슨 요일인지는 입력으로 주어집니다. 
이 때 일을 표기하는데 0부터 9까지의 각 숫자를 각 색상으로 몇 번씩 쓰게 되는지 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 SUN, MON, TUE, WED, THU, FRI, SAT 중 하나가 주어집니다.
각각 1월 1일이 일요일, 월요일, 화요일, 수요일, 목요일, 금요일, 토요일인 경우를 의미합니다.
둘째 줄에 주문자가 명시한 공휴일의 수 N이 주어집니다. (1 ≤ N ≤ 365)
다음 N개의 줄에 걸쳐 두 정수 a, b가 공백으로 구분되어 주어집니다.
주문자가 a월 b일을 공휴일로 지정해달라고 명시했음을 의미합니다.
a월 b일이 존재하지 않거나 같은 날을 두 번 이상 지정하게 되는 경우는 주어지지 않습니다.

[출력]
총 10개의 줄을 출력합니다.
i번째 줄에는 숫자 i - 1을 빨간색으로 표기한 횟수, 파란색으로 표기한 횟수, 검은색으로 표기한 횟수를 공백으로 구분하여 출력합니다.
'''
'''
[설계]
각 월의 말일을 저장해놓고, 전부 탐색
토요일 또는 평일은 휴일인지 확인

빨, 파, 검으로 각 숫자마다 count
'''
def count_color(date, color_str):  # 0 빨, 1 파, 2 검
    global color_cnts
    color = 0
    if color_str == 'blue':
        color = 1
    elif color_str =='black':
        color = 2

    if date < 10:
        color_cnts[date][color] += 1
    else:
        one = date%10
        ten = int(date/10)
        color_cnts[one][color] += 1
        color_cnts[ten][color] += 1


weekday = input()
N = int(input())

holiday = set()
for _ in range(N):
    # 4자리로 날짜 표현 8월 10일 이면 810
    mon, date = map(int, input().split())
    code = mon*100 + date 
    
    holiday.add(code)

end_dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday_num = {'SUN':0, 'MON':1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6}
color_cnts = [[0, 0, 0] for _ in range(10)]  # 빨, 파, 검

current_weekday = weekday_num[weekday]
current_month = 1
current_date = 1
while True:
    code = current_month*100 + current_date
    if (current_weekday == 0) | (code in holiday):  # 일요일 or 공휴일
        count_color(current_date, 'red')
    elif current_weekday == 6:  # 토요일
        count_color(current_date, 'blue')
    else:
        count_color(current_date, 'black')

    if (current_month == 12) & (current_date == end_dates[12]): break

    current_weekday = (current_weekday + 1) % 7
    current_date += 1
    if current_date > end_dates[current_month]:  # 마지막 날을 넘기면 다음 월로 넘어감
        current_month += 1
        current_date = 1

# 정답
for i in range(10):
    print(color_cnts[i][0], color_cnts[i][1], color_cnts[i][2])


