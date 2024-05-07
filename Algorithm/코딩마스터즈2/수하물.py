N, M = map(int, input().split())  # 물건 개수, 가방 개수

items = []  # (무게, 가격)
for i in range(N):
    w, v = map(int, input().split())
    items.append((w,v))

bags = []  # 제한 무게
for i in range(M):
    w = int(input())
    bags.append(w)

# 낮은 가방부터 최대 가치를 담아나간다 -> 그리디
items = sorted(items, key = lambda x: -x[1])
bags = sorted(bags)


sum = 0
used = [0]*(N+1)  # 아이템이 담겼는지 확인
for bag in bags:
    for i, item in enumerate(items):
        if used[i] == 1:  # 이미 아이템이 가방에 담겨있다면 skip
            continue

        if bag >= item[0]:
            sum += item[1]
            used[i] = 1
            break

print(sum)     


