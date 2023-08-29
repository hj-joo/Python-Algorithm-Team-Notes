def binary_search(value, arr, start ,end):
    if start > end:
        return
    mid = (start + end) // 2
    # print(mid)
    if arr[mid] == value:
        return mid
    
    elif arr[mid] > value:
        return binary_search(value, arr, start, mid - 1)
    
    else:
        return binary_search(value, arr, mid + 1, end)  
        
# n(원소의 개수)과 target( 찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 워소 입력 받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
result = binary_search(target, array, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    