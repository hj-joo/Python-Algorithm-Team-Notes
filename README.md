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
[DFS/BFS](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/DFS\BFS)
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
## String 처리

* [String_Manipulation](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/String_Manipulation)
* 문자열 처리 꿀팁!
```
# 문자열 있는지 확인
# 문자열 안에 a라는 문자열이 포함되는지 -> in쓰면 됨
if a in string:
	pass

# 아스키 코드 활용
# 만약 A를 숫자로 바꾸고 싶다?
alpha = 'A'
int(ord(alpha)) - int(ord('A')) + 1

# 알파벳인지 확인
alpha.isalpha() # --> True면 알파벳

# 숫자인지 확인
digit.isdigit()

# 알파벳, 숫자 확인
alnum.isalnum()

# 문자열 팰린드롬
s==s[::-1]

# 문자열 공백없이 나열하는 방법
print(''.join(string))

# 문자열 변경 및 제거 re.sub
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
words = re.sub('[^\w]', ' ', paragraph.lower()).split() # 1번째 인자 -> \w(단어) ^ 아닌거,  2번째 인자 -> 공백으로 변경, 3번째 인자 -> .lower() 소문자 변경, split() 공백 기준 분리

# 문자열 개수 세기
from collections import Counter
counts = Counter(words)
# 제일 첫번째로 많이 카운트 된 단어 소환
counts.most_common(1)[0][0]
```

## Sorting
* [Sorting](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/Sorting)
* 사실 sort()나 sorted()만 써도 충분하긴 함..

## Binary_Search
* [Binary_Search](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/Binary_Search)
* 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
	* 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
	* 이진 탐색 개꿀팁! -> from bisect import bisect_left, bisect_right
	* bisect_left(arr, value) --> 왼쪽 인덱스 반환	
	* bisect_right(arr, value) --> 오른쪽 인덱스 반환	

## Dynamic_programming
* [Dynamic_programming](https://github.com/hj-joo/Python-Algorithm-Team-Notes/tree/main/Dynamic_programming)
* 다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법.
* 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함. -> 완전 탐색 문제를 효율적으로 풀 수 있음.
* 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성.
    1. 최적 부분 구조
        * 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결
    2. 중복되는 부분 문제
        * 동일한 작은 문제를 반복적으로 해결
* 메모이제이션(탑다운, 하향식)
    * 한 번 계산한 결과를 메모리 공간에 메모하는 기법 -> 캐싱!
* 보텀업(상향식)
    * DP 테이블
* 그리디, 구현, 완전 탐색으로 접근해보고 안되면 다이나믹 프로그래밍 접근
* 재귀 함수로 작성해보고 여기서 코드를 개선 -> 다이나믹 프로그래밍

* DP인지 확인하는 두 가지 방법
    1. **DFS/BFS로 풀 수 있지만, 경우의 수가 너무 많은 경우**
    2. **경우의 수들에 중복적인 연산이 많은 경우**
* **DP식 사고방식**
    * 연산을 반복안하려면 어떤 정보를 남겨야할까? 
    * 나만의 자료구조를 만들고 어떤 정보를 담을지 고민하는 것.
* **점화식을 잘 세워야 한다. DP는 점화식만 세우면 됨!**

> To be continue...
# Reference
* [동빈나 깃허브](https://github.com/ndb796/python-for-coding-test)
* [동빈나 유튜브](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)
* [파이썬 알고리즘 인터뷰](https://github.com/onlybooks/algorithm-interview)
