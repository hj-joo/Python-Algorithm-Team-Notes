'''
• 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있습니다. 
이 공간은 1 x 1 크기의 정사각형으로 나누 어져 있습니다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 
여행가 A 는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. 우리 앞에는 여행가 A가 이동 할 계획이 적힌 계획서가 놓여 있습니다.

• 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니 다. 각 문자의 의미는 다음과 같습니다.
    • L: 왼쪽으로 한 칸 이동
    • R: 오른쪽으로 한 칸 이동
    • U: 위로 한 칸 이동
    • D: 아래로 한 칸 이동
'''


n = int(input())

data = input().split()

x, y = 1, 1
# 오 위 왼 아
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# for direction in data:
#     if direction == 'R':
#         x = x + dx[0]
#         y = y + dy[0]
#     if direction == 'U':
#         x = x + dx[1]
#         y = y + dy[1]
#     if direction == 'L':
#         x = x + dx[2]
#         y = y + dy[2]
#     if direction == 'D':
#         x = x + dx[3]
#         y = y + dy[3]
#     # if x < 1 or y < 1:
        
        
# print(x, y)

move_types = ['R', 'U', 'L', 'D']

for direction in data:
    for i in range(len(move_types)):
        if direction == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    
print(x,y)