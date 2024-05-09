'''
악성 사용자가 제목으로 사용한 서로 다른 두 개의 문장이 입력으로 주어집니다. 
두 문장의 길이는 같으며, 한 쪽에서 등장한 단어는 반드시 다른 쪽에서도 등장합니다. 
문제의 상황을 단순하게 만들기 위해 한 문장에 같은 단어가 여러번 등장하는 경우는 주어지지 않습니다. 
두 단어의 자리를 바꾸면 주어진 두 개의 문장을 모두 만들 수 있는 문장이 몇개인지 출력하는 프로그램을 작성하세요.

[입력]
첫째 줄에 악성 사용자가 제목으로 사용한 문장에 등장하는 단어의 수 N이 주어집니다. (3 ≤ N ≤ 5,000)
둘째 줄에 악성 사용자가 제목으로 사용한 첫번째 문장이 주어집니다.
셋째 줄에 악성 사용자가 제목으로 사용한 두번째 문장이 주어집니다.
모든 단어의 길이는 1 이상 5 이하입니다.

[출력]
문제의 정답을 출력합니다.

[설계]
두 문장을 비교해서 다른 위치의 단어를 각각 list에 넣는다.
최대 4개의 단어가 다를 것이다.

첫번째 list에서 위치를 바꿔 가능한 순서를 dict에 넣는다.
두번째 list에서 위치를 바꿔 가능한 순서를 기존 dict과 비교하여 존재하면 cnt 한다.

처음 두 문장을 비교하는 시간 5천번*문장길이(5) 정도  2만 5천
'''
N = int(input())
words1 = input().split()
words2 = input().split()

diff1 = []
diff2 = []
for i in range(N):
    if words1[i] != words2[i]:
        diff1.append(words1[i])
        diff2.append(words2[i])

sentence_set = set()
for first in range(len(diff1)-1):
    for second in range(first + 1, len(diff1)):
        # 바꿀 두 개의 단어를 고른다.
        sentence = ''
        for i in range(len(diff1)):
            if i == first:
                sentence += diff1[second]
            elif i == second:
                sentence += diff1[first]
            else:
                sentence += diff1[i]
        sentence_set.add(sentence)

ans = 0
for first in range(len(diff2)-1):
    for second in range(first + 1, len(diff2)):
        # 바꿀 두 개의 단어를 고른다.
        sentence = ''
        for i in range(len(diff2)):
            if i == first:
                sentence += diff2[second]
            elif i == second:
                sentence += diff2[first]
            else:
                sentence += diff2[i]
        if sentence in sentence_set:
            ans += 1
print(ans)