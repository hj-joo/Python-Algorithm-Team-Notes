# 이진 탐색 라이브러리
# bisect_left(arr, value) -> 이진 탐색 후 왼쪽 인덱스 반환
# bisect_right(arr, value) -> 이진 탐색 후 오른쪽 인덱스 반환

# from bisect import bisect_left, bisect_right

# # 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left_index

# # 배열 선언
# a= [1,2,3,3,3,3,4,4,8,9]

# # 값이 4인 데이터 개수 출력
# print(count_by_range(a, 4, 4))

# # 값이 1-1, 31 범위에 있는 데이터 개수 출력
# print (count_by_range(a, -1, 3))

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = list(map(int, input().split()))

def count_element(a,x):
    result = bisect_right(a,x) - bisect_left(a,x)
    # print(result)
    if result == 0:
        result = -1

    return result
print(count_element(a,x))