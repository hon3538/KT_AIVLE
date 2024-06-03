'''
각 네트워크의 컴퓨터는 M개로 구성되고 번호는 허브 컴퓨터 번호부터 1씩 추가한 값이다.
각 허브 컴퓨터는 0번 중앙컴퓨터에 연결되어 있다.

연결된 컴퓨터 사이만 접속이 가능하다고 할 때, 올바른 접속인지 판별하는 프로그램 작성해라.

허브 컴퓨 번호는는 1, 1+M, 1+2M, ..., 1+(N-1)M


[설계]
컴퓨터의 번호를 보고 네트워크 번호와 허브 컴퓨터 여부를 알고
이전 로그와 이후 로그를 비교하여 연결된 컴퓨터인지 판단하여 결과 산출
허브-중앙 관계인가?
아니면 같은 네트워크인가?
아니면 비정상 접속

중앙 컴퓨터: 0
컴퓨터 번호: 번호/M + 번호%M 
네트워크 번호: 번호/M -> 번후%M의 결과가 0이라면 -1 더해주기  1~M -> 1번 네트워크, M+1~2M -> 2번 네트워크
허브 컴퓨터 여부: 번호%M == 1
네트워크 번호가 곧 허브 컴퓨터 번호  

'''
N, M = map(int, input().split())  # 허브 컴퓨터 개수, 네트워크 별 컴퓨터 개수
K = int(input())  # 접속 log 개수
logs = list(map(int, input().split()))  # 접속 로그 0 -> 1 -> 2 -> 3..

ans = 'YES'
for i, log in enumerate(logs[:-1]):
    now = log
    next = logs[i+1] 

    # 허브 - 중앙 관계인가 ? 
    if (now%M + next == 1) | (now + next%M == 1):
        continue 
    
    # 같은 네트워크 인가?
    network1 = int(now/M)
    if now%M == 0:
        network1 -= 1 
    
    network2 = int(next/M)
    if next%M == 0:
        network2 -= 1
    
    if network1 != network2:
        ans = 'NO'
        break

print(ans)