# 삽입 정렬
# 첫 번째 데이터는 그 자체로 정렬되어있다고 판단, 그 다음 데이터가 어디로 갈지 판단하여 삽입
# O(n^2), 최선의 경우(거의 정렬되어 있는 상태) O(n)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽 이동 
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터 만나면 멈춤
            break
        
print(array)