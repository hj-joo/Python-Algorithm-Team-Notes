'''
• N가지 종류의 화폐가 있습니다. 
이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다. 
이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
• 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한 의 화폐 개수입니다.
• M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

2 15
2
3

'''
'''
• ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
• k= 각 화폐의 단위
• 점화식: 각 화폐 단위인 k를 하나씩 확인하며
• ai-k를 만드는 방법이 존재하는 경우, ai = min(ai, ai-k + 1)
• ai-k를 만드는 방법이 존재하지 않는 경우, ai = INF
'''
n, m = map(int, input().split())

#화폐 정보
array = []
for i in range(n):
    array.append(int(input()))
    
# DP초기화
dp = [10001]*(m+1)
    
dp[0] = 0
for i in range(n): 
    for j in range(array[i], m+1):
        if dp[j-array[i]] != 10001: # i-k원을 만드는 방법이 존재하지 않는 경우
            dp[j] = min(dp[j], dp[j-array[i]]+1)
            
            
if dp[m] == 10001:
    print(-1)

else:
    print(dp[m])