'''
팬그램은 알파벳의 모든 글자를 사용하여 만든 문장을 말합니다. 
공백이 없는 문자열이 주어졌을 때, 
이 문자열이 팬그램인지 여부를 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 문자열이 주어집니다.
문자열의 길이는 100이하이며, 알파벳 대문자와 소문자로만 이루어져 있습니다.

[출력]
문자열이 팬그램이면 "YES", 그렇지 않으면 "NO"를 출력합니다.
'''
alpha_set = set()

s = input()
s = s.lower()

cnt = 0
for i in s:
    if i not in alpha_set:
        alpha_set.add(i)
        cnt +=1

if cnt == 26:
    print('YES')
else:
    print('NO')
