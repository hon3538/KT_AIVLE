'''
#RRGGBB
RGB의 16진수 값의 평균으로 채워넣기
'''
'''
[설계]
10진수 변환기
16진수 변환기
'''
def to_decimal(hex_str):
    pos_1 = 0
    if (ord(hex_str[1]) >= ord('A')) & (ord(hex_str[1]) <= ord('F')):
        pos_1 = ord(hex_str[1]) - ord('A') + 10
    else:
        pos_1 = int(hex_str[1])
    
    pos_10 = 0
    if (ord(hex_str[0]) >= ord('A')) & (ord(hex_str[0]) <= ord('F')):
        pos_10 = ord(hex_str[0]) - ord('A') + 10
    else:
        pos_10 = int(hex_str[0])
    pos_10 *= 16

    return pos_10 + pos_1

def to_hex(num):
    pos_1 = ''
    if num%16 >= 10:
        pos_1 = chr(ord('A') + num%16 - 10)
    else:
        pos_1 = str(num%16)
    
    num = int(num/16)
    pos_10 = ''
    if num%16 >= 10:
        pos_10 = chr(ord('A') + num%16 - 10)
    else:
        pos_10 = str(int(num)%16)

    return pos_10 + pos_1

input_str = input()
R = input_str[1:3]
G = input_str[3:5]
B = input_str[5:7]

R_n = to_decimal(R)
G_n = to_decimal(G)
B_n = to_decimal(B)

mean_val = round((R_n + G_n + B_n)/3)
hex = to_hex(mean_val)


print(f'#{hex}{hex}{hex}')