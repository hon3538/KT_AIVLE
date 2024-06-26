'''
1. 문자열의 왼쪽부터 문자열의 각 문자가 몇 번째 알파벳인지 알아낸다. 이 수를 a라고 하자.
2. a가 9 이하라면 a를 그대로 쓰고, a가 10 이상이라면 a를 쓰고 그 뒤에 0을 붙인다.

예를 들어, "park"를 인코딩하면 다음과 같이 진행됩니다.

1. p는 16번째 알파벳이다. 16을 쓴 후, 뒤에 0을 붙여서 160을 쓴다. (160)
2. a는 1번째 알파벳이다. 1을 쓴다. (1601)
3. r은 18번째 알파벳이다. 18을 쓴 후, 뒤에 0을 붙여서 180을 쓴다. (1601180)
4. k는 11번째 알파벳이다. 11을 쓴 후, 뒤에 0을 붙여서 110을 쓴다. (1601180110)

따라서, park를 인코딩한 결과는 1601180110입니다.
인코딩 결과가 주어졌을 때, 디코딩하시오

[설계]
문자의 순서인지 인코딩의 숫자인지 구분하는 방법
-> 0으로 나눈다? : 10, 20 번째 문자도 있으므로 애매
-> 숫자를 뒤에서부터 참조하여 0이 나오면 앞 두 자리는 문자를 가리키는 숫자이다.
-> 그 두자리 수 다음 수를 참조하여 0이 아니면 문자를 가리키는 숫자이다.
'''
def to_alphabet(num_str):
    num = int(num_str)
    return chr(ord('a')+num-1)

encoding = input()
ans = ''
pos = len(encoding) - 1
while pos >= 0:
    if encoding[pos] == '0':
        alpha = to_alphabet(encoding[pos-2:pos])
        pos -= 3  # 0과 두 개의 숫자를 봤으니 -3 
    else:
        alpha = to_alphabet(encoding[pos])
        pos -= 1
    ans = alpha + ans
print(ans)