'''
• n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 
각 칸은 특정한 크기의 금이 들어 있습니다.
• 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 
이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이 동해야 합니다. 
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
'''
• array[i][j]= i행 j열에 존재하는 금의 양
• dp[i][j] =i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
• 점화식은 다음과 같습니다.
    dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
• 이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 합니다.
• 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됩니다.
• 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용할 수 있습니다.
'''

T = int(input())

for i in range(T):
    
# gold = []    
    n,m = map(int, input().split())
    temp = list(map(int, input().split()))
    dp = []
    index = 0

    for i in range(n):
        dp.append(temp[index:index+m])
        index +=m

    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우 
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
# print(gold)
