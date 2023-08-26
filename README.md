# Python-Algorithm-Team-Notes
(개인 공부)코딩 테스트를 위한 자주 사용하는 알고리즘 라이브러리화
## Greedy
* [Greedy](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/Greedy)
## Implementation
* [Implementation](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/Implementation)
* 2차원 배열 꿀팁
```
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 공식처럼 외워두면 좋을 듯
for i in range(4):
	nx = x+dx[i]
	ny = y+dy[i]
```

## DFS/BFS
* 스택 자료구조: **선입후출**, 프링글스 과자통, 파이썬에서는 리스트로 **append, pop()**으로만 구현 가능
```
stack = []
stack.append(5)
stack.append(2)
stack.pop()
print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```
* 큐 자료구조: LoL 큐 잡혔다, **선입선출**, 파이썬에선 **deque로 큐를 구현**하는게 효율적. **append, popleft**로 구현.
```
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.popleft()
print(queue)
queue.reverse()
print(queue)
```
* 재귀함수: 함수 안에 함수 안에 함수 안에 함수 안에 ... 일종의 스택구조로 생각 하면 됨
```
def recursive_func():
	print("재귀함수")
	recursive_func()
 
recursive_func()
```

* DFS(Depth-First Search) -> 스택, 재귀 사용
```
# DFS 메서드 정의
def dfs(graph, v, visited):
# 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph [v]:
        if not visited[i]:
            dfs(graph, i, visited)
```
* BFS(Breadth-First Search) --> 큐 자료구조
```
# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]: 
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

> To be continue...
# Reference
* [동빈나 깃허브](https://github.com/ndb796/python-for-coding-test)
* [동빈나 유튜브](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)
