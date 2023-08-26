'''
• N X M 크기의 얼음 틀이 있습니다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다. 
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있은 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요. 
다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

00110
00011
11111
00000

'''

def dfs(x, y):
    
    if x < 0 or y<0 or x>n-1 or y>m-1:
        return False
    
    if ice_graph[x][y] ==0:
        ice_graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False
        

n, m = map(int, input().split())

ice_graph = []

for i in range(n):
    ice_graph.append(list(map(int, input())))

# print(ice_graph)

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1

print(result)