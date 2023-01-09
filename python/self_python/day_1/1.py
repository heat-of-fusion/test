# print('# 하나만 출력합니다')
# print('Hello Python Programming...!')
# print()
# print('# 여러 개를 출력합니다.')
# print(10, 20, 30, 40, 50)
# print('안녕하세요', '저의', '이름은', '박제현입니다!')
# print()
# print('#아무것도 출력하지 않습니다.')
# print('---확인 전용선---')
# print()
# print()
# print('---확인 전용선---')

# print(type('안녕하세요'))
# print(type(123))

# print('"안녕하세요"라고 말했습니다')
# print("'배가 고픕니다'라고 생각했습니다")

# print('문자를 뒤에서부터 선택해볼까요?')
# print('안녕하세요'[-1])
# print('안녕하세요'[-2])
# print('안녕하세요'[-3])
# print('안녕하세요'[-4])
# print('안녕하세요'[-5], '\n')

# print('안녕하세요'[0])
# print('안녕하세요'[1])
# print('안녕하세요'[2])
# print('안녕하세요'[3])
# print('안녕하세요'[4])

# print('안녕하세요'[1:4])
# print('안녕하세요'[1:])

# n = int(input())
# for i in range(n):
#     n1, n2 = map(int, input().split())
#     print('Case #%d: '%(int(i)+1), n1+n2)

# n = int(input())
# arr = []
# for i in range(n):
#     n1, n2 = map(int, input().split())
#     arr.append(n1)
#     arr.append(n2)
# for i in range(n):
#     print('Case #%d:'%(i+1), arr[int(i)*2]+arr[int(i)*2+1])

# n_list = []
# n = int(input())
# for i in range(n):
#     n1, n2 = map(int, input().split())
#     n_list.append(n1)
#     n_list.append(n2)
# for i in range(n):
#     print('Case #%d: %d + %d = %d'%(i+1, n_list[i*2], n_list[i*2+1], n_list[i*2] + n_list[i*2+1]))

import datetime
d = datetime.datetime.now()
if d.month < 10:
    print('%d-0%d-%d'%(d.year, d.month, d.day))