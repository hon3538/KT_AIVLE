'''
준하는 어떤 수 하나를 들고 가는 중 실수로 땅에 떨어뜨리고 말았습니다.
땅에 떨어진 수는 여러 개의 숫자들로 분리되었고, 
준하는 이 숫자들을 황급히 주워 담기 시작했습니다.

준하는 주워담은 숫자 중 빠진 것이나 원래 갖고 있지  않은 것이 섞여 있지는 않는지 궁금해졌습니다.
준하를 위해 이를 해결해 주는 프로그램을 작성하세요.

[입력]
첫째 줄에 준하가 떨어뜨린 수가 주어집니다. 수의 길이는 10이하 입니다.
둘째 줄에 준하가 주워담은 숫자들이 주어집니다.

[출력]
준하가 숫자들을 제대로 회수했다면 "YES", 그렇지 않다면 "NO"를 출력합니다.
'''
'''
[설계]
map에 넣고 count하여 두 개의 숫자 리스트를 비교한다.
'''
num1 = input()
num2 = input()

map1 = dict()
map2 = dict()

for c in num1:
    if not c in map1:
        map1[c] = 1
    else:
        map1[c] += 1

for c in num2:
    if not c in map2:
        map2[c] = 1
    else:
        map2[c] += 1

ans = 'YES'
for o in range(ord('0'), ord('9')+1):
    c = chr(o)

    if map1.get(c) != map2.get(c):
        ans ='NO'
        break
print(ans)