import time
import re
# 1번 풀이(리스트)
# 타입 힌트를 주는 것 -> 좋은 코드 작성 방식
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        # isalnum() -> 영문자, 숫자 여부를 판단하는 함수
        if char.isalnum():
            # lower() -> 모두 소문자로 변환하는 함수
            strs.append(char.lower())
            
    while len(strs) > 1:
        # 맨 앞의 문자와 맨 뒤의 문자를 하나씩 빼서 확인
        if strs.pop(0) != strs.pop():
            return False
        
    return True

start = time.time()
print(isPalindrome("A man, a plan, a canal: Panama"))
print(f'List: {time.time()-start}')


# 2번 풀이(데크)
from collections import deque
def isPalindrome_deque(s: str) -> bool:
    q = deque()
    for char in s:
        if char.isalnum():
            q.append(char.lower())

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True
            
start = time.time()
print(isPalindrome_deque("A man, a plan, a canal: Panama"))
print(f'Deque: {time.time()-start}')

# 3번 풀이(슬라이싱)

def isPalindrome_slicing(s: str) -> bool:
    s = s.lower()
    
    # 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1] # 슬라이싱
            
start = time.time()
print(isPalindrome_slicing("A man, a plan, a canal: Panama"))
print(f'Deque: {time.time()-start}')        