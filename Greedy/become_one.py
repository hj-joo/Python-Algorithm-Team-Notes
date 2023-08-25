'''
문제
• 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
    1. N에서 1을 뺍니다.
    2. N을 K로 나눕니다.
• 예를 들어 No 17. K가 4라고 가정합시다. 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다. 이후에
2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 30 됩니 다. 이는 N을 1로 만드는 최소 횟수입니다.
• N과 K가 주어질 때 NOl 10 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그 램을 작성하세요.

입력조건
•• 첫째 줄에 N(1 (= N (= 100,000)과 K(2 (= K (= 100,000)가 공백을 기준으로 하여 각각 자연수
로 주어집니다.
출력 조건
• 첫째 줄에 No 1 이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다.
'''

import time

# 내 풀이
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())


start = time.time()
# n = 25
# k = 3
count = 0

while True:
    if n%k ==0:
        n = n//k

    else:
        n = n-1
        
    count +=1
    if n == 1:
        break
print(count)





# # 동빈나 풀이
# # 로그 시간 복잡도로 가능

# result = 0

# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k
    
# # 마지막으로 남은 수에 대하여 1씩 빼기

# result += (n - 1)
# print(result)


end = time.time()

print(f"{end - start:.5f} sec")