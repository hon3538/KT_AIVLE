'''
연구실에는 N개의 용액이 존재합니다.
각 용액은 A 타입, B 타입, C 타입 중 하나입니다. 
현재 철수는 세 가지 타입의 용액을 섞어 신소재를 개발할 수 있는지 실험하고 있습니다.

실험 과정은 다음과 같습니다.

1. 실험 시작 시, 비커는 비어있습니다.
2. 용액 한 개를 선택해 비커에 모두 투입합니다.
3. N개의 용액을 모두 소모하면 실험이 종료됩니다.

간단한 실험이지만 주의해야 할 사항이 있습니다. 
직전에 투입한 용액과 같은 타입의 용액을 연속해서 투입하면 사고가 발생합니다.

[입력]
첫째 줄에 양의 정수 A, B, C가 공백으로 구분되어 주어집니다.
이는 각 타입 용액의 개수를 의미합니다. (1 ≤ A, B, C ≤ 10,000)

[출력]
첫째 줄에 사고 발생 없이 실험을 끝마칠 수 있으면 "YES"를, 그렇지 않으면 "NO"를 출력합니다. (큰 따옴표 제외)

[설계]
순서대로 가장 많은 용액을 먼저 투입, 용액 하나가 다른 용액 하나를 상쇄시킬 수 있다.
예를 들어 A 1000개, B 500개, C 500개 이면 A - B - C = 0 으로 만들 수 있다.
또는 A 1000개, B 500개, C 700개 이면 A로 B 400개, C 600개 상쇄시키고 B - C 가 서로 100개씩 상쇄시키면 된다.
조건? 하나의 숫자가 두 숫자를 합친 것보다 크면 안 된다.

A 5, B 2, C 2 도 가능
A B A B A C A C A..
total - max + 1 < max 이면 불가능

-> 문제상황 없는지?
-> 연속으로만 배치 안 되면 돼..

'''

liquids = list(map(int, input().split()))  # A, B, C

total = sum(liquids)

ans = 'YES'
for l in liquids:
    if (total - l) + 1 < l:
        ans = 'NO'
print(ans)

    




