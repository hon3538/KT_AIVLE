'''
[설계]
연속한 날의 이익이 최대가 되는 날 구하기 
sliding window -> 5000 * 5000
-> 시간 초과

이익이 - 10000까지 날 수 있으므로
모든 이익에 +10000 해주고 two pointer로 가변하면서 탐색
-> 어떻게 가변할 건데, 기준이 없음

압축기법
+의 연속구간은 하나로 합쳐도 된다. 푸드트럭 빌리는 일수에 제한이 없음
'''

N = int(input())  # 축제 기간 5000
profits = list(map(int, input().split()))  # 각 날의 예측 이익

compressed = []
l = 0  # 연속된 구간 길이
prev = profits[0]
val = 0

ans = -0x7fffffff
for profit in profits:
    if prev * profit < 0:  # 서로 부호가 달라졌다는 뜻
        compressed.append([l, val])  # 길이, 값
        l = 0
    l += 1
    val += profit
    if ans < profit:
        ans = profit
        
compressed.append([l, val])  # 마지막

prefix_sum = []  # 길이, 값 list로 저장
len_sum = 0
val_sum = 0
index = 0
for l, v in compressed:
    prefix_sum.append([len_sum + l, val_sum + v])
    val_sum = prefix_sum[index][1]
    index += 1

for size in range(1, len(compressed)):
    for head in range(0, len(compressed)-size+1):
        end = head + size - 1
        profit = prefix_sum[end][1] - prefix_sum[head][1] + compressed[head][1]
        if ans < profit:
            ans = profit
         
print(ans)
            
    