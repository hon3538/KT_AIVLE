'''
치훈은 팔찌를 여러 개 가지고 있습니다.
팔찌는 1개 이상의 보석들이 원형으로 배열되어 있는 형태입니다. 

팔찌 2개의 보석 배열 상태가 주어졌을 때,
두 팔찌가 같은 팔찌인지 판별하는 프로그램을 작성하세요.

두 팔찌가 같다는 것은, 팔찌를 회전하여 같은 형태로 만들 수 있다는 것을 말합니다.
단, 팔찌를 뒤집을 수는 없습니다.

[입력]
팔찌 2개가 두 줄에 걸쳐 주어집니다.
각 팔찌는 알파벳 대문자로 이루어진 문자열의 형태로 주어집니다.
같은 문자는 같은 보석을 뜻합니다.
문자열의 길이는 1000 이하입니다.

[출력]
두 팔찌가 같으면 YES, 다르면 NO를 출력합니다.
'''
'''
[설계]
하나의 팔찌를 돌려가면서 비교, 최대 1000번
'''

ring1 = input()
ring2 = input()
length = len(ring2)

ans = 'NO'
for _ in range(length):
    if ring1 == ring2:
        ans = 'YES'
        break

    ring2 = ring2[1:] + ring2[0]

print(ans)

