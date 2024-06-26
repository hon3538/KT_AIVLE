'''
서울은행은 새로운 펀드 상품을 개발했습니다. 
이 펀드 상품은 상품의 기본 금액과 신용도를 기반으로 예상 수익을 돌려받을 수 있는 상품입니다. 
이때, 구매자는 여러 개의 옵션들을 펀드에 적용시켜 예상 수익을 늘릴 수 있습니다. 
구매자는 N개의 옵션들 중, 정해진 개수의 옵션들을 최대 M개까지 적용시킬 수 있습니다.
예상 수익 금액은 (상품의 기본 금액 + 상품의 신용도 * 옵션의 금액의 합)입니다.
구매자가 낼 수 있는 가장 높은 예상 수익 금액을 구하세요.

[입력]
첫째 줄에 펀드 상품의 기본 금액 A와 신용도 B가 서로 공백을 두고 자연수로 주어집니다. (1 ≤ A, B ≤ 1,000)
둘째 줄에 옵션의 개수 N과 선택할 옵션의 개수 M이 공백을 두고 주어집니다. 이때의 N, M은 다음의 조건을 따릅니다. 1<= N <= M <= 100
셋째 줄부터 N개의 줄에 걸쳐 각 옵션 금액이 주어집니다. 금액은 10,000 이하의 자연수입니다.

[출력]
가장 높은 예상 수익을 출력합니다.
'''
'''
[설계]
옵션을 내림차순정렬하고 M개 만큼 합을 구한다
'''

A, B = map(int, input().split())  # 기본 급액, 신용도
N, M = map(int, input().split())  # 전체 옵션 개수, 선택 옵션 개수

options = []
for _ in range(N):
    price = int(input())
    options.append(price)

options = sorted(options, reverse=True)
options_price = sum(options[:M])

ans = A + B*options_price
print(ans)