'''
"입력 파일의 크기가 M보다 크지 않게 해주세요."

기성이 만든 문제의 입력 파일에는 공백으로 구분된 정수 N개가 저장되어 있습니다. 
i번째 정수가 L[i]자리 수라면, 
입력 파일의 크기는 L[1] + L[2] + … + L[N-1] + L[N] + (N - 1)입니다. 
N - 1은 공백이 차지하는 크기입니다. 
예를 들어 입력 파일 "1 2 30 123"의 크기는 10입니다.

그런데, 입력 파일의 크기가 M보다 큰 것 이였습니다. 
기성은 이 문제를 해결하기 위해 정수를 10진법 대신 다른 진법으로 표기하기로 했습니다. 
10진법 정수 123(= 1 × 10² + 2 × 10¹ + 3 × 10⁰)은 12진법으로 A3(= A × 12¹ + 3 × 12⁰)으로 표기하고, 40진법으로 33(= 3 × 40¹ + 3 × 40⁰)으로 표기합니다. 
10진법 0부터 9까지는 똑같이 0부터 9로, 10부터 35까지는 A부터 Z까지의 대문자 알파벳으로, 36부터 61까지는 a부터 z까지의 소문자 알파벳을 사용합니다.

예를 들어 입력 파일 "1 2 30 123"을 12진법으로 표기하면 "1 2 26 A3"이 되어 파일의 크기가 9로 줄어듭니다. 
입력 파일의 크기가 M 이하가 되는 10 이상의 가장 작은 진법을 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 두 정수 N과 M이 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 1,000)
둘째 줄에 기성이의 입력 파일이 주어집니다. (1 ≤ 입력 파일의 모든 정수 ≤ 100,000)
기성의 입력 파일의 정수는 모두 10진법으로 작성되어 있습니다.

[출력]
입력 파일의 크기가 M 이하가 되는 10 이상의 가장 작은 진법을 출력합니다.
만약 62진법으로 표기해도 입력 파일의 크기가 M보다 크다면 대신 -1을 출력합니다.
'''
'''
[설계]
10~62 진법까지 순차적으로 확인
각 진법 당 변환 횟수 N번 + 길이 확인 N번

총 2N * 50 = 1만번으로 가능
'''
def num2char(num):  # 숫자를 정해진 규칙에 따른 문자로 변환
    if num < 10:
        return chr(ord('0') + num)
    elif num < 36:
        return chr(ord('A') + num - 10)
    elif num < 62:
        return chr(ord('a') + num - 36)
    else: 
        return -1

def num2str(way, num):  # 해당 숫자를 정해진 진법으로 변환
    num_str = num2char(num%way)

    while int(num/way) != 0:  # 몫이 없을 떄 까지
        num /= way
        num_str = num2char(int(num%way)) + num_str

    return num_str

    
def get_size(way, num_list):  # 진법(way)와 num list가 주어졌을 때, 파일 크기 출력
    num_list_str = num2str(way, num_list[0])
    for num in num_list[1:]:
        num_str = num2str(way, num)
        num_list_str = ' '.join([num_list_str, num_str])

    return len(num_list_str)

N, M = map(int, input().split())  # 정수 개수, 파일 제한 크기
num_list = list(map(int, input().split()))
ans = -1


for i in range(10, 63):  # 62 진법까지 가능
    size = get_size(i, num_list)
    
    if size > M:
        continue

    ans = i
    break
    
print(ans)
