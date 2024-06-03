'''
빨간색, 초록색, 파란색 상자에 3개의 짐을 넣고
두 개의 상자에 들어있는 짐을 10^18번 바꿨을 때
각 상자색에 맞게 짐을 넣을 수 있는 지 여부

[설게]
상자와 짐의 색깔이 다른 것이 2개라면 홀수번
상자와 짐의 색깔이 다른 것이 3개라면 짝수번 섞어야 한다.

'''
boxes = list(input().split())  # 0빨, 1초, 2파
colors = ['R', 'G', 'B']
diff_cnt = 0
for i, box in enumerate(boxes):
    if box != colors[i]:
        diff_cnt += 1

if diff_cnt == 2:
    print('impossible')
else:
    print('possible')

