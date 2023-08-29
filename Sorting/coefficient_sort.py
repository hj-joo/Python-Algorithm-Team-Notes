# 특정 조건에 부합할 때 사용하는 정렬 알고리즘
# 인덱스 개수를 활용
# 데이터 크기 범위가 제한이며, 정수일 때 매우 효율적
# 최악의 경우, O(n+k)

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def coefficient_sort(array):
    
    cof_arr = [0 for _ in range(min(array), max(array)+1)]
    for cof in array:
        cof_arr[cof] += 1
    
    # print(cof_arr)
    for i, v in enumerate(cof_arr):
        for result in range(v):
            print(i, end=" ")
        

coefficient_sort(array)

'''
• 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 0(N + K)입니다.
• 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있습니다.
• 데이터가 0과 999,999로 단 2개만 존재하는 경우를 생각해 봅시다.
• 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있습니다.
• 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적입니다.
'''