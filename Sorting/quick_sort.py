# 퀵 정렬
# 기준 데이터 설정, 기준보다 큰 데이터와 작은 데이터의 위치를 변경
# 보통 첫 번째 데이터로 기준 Pivot 설정
# 평균 O(nlogn), 최악 O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start +1
    right = end
    
    while(left <= right):
        while(left <= end and arr[left] <= arr[pivot]):
            left +=1
        while(right > start and arr[right] >= arr[pivot]):
            right -=1
        if(left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
        
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)