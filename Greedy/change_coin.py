# 거스름 돈 문제
'''
문제
당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원,
10원짜리 동전이 무한히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어 야 할 동전의 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.
'''

'''
풀이
• 최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 주면 됩니다.
• N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러 줍니다.
• 이후에 100원, 50원, 10원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 주면 됩니다.
• N = 1,260일 때의 예시를 확인해 봅시다.

• 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는 무엇일까요?
• 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른
해가 나올 수 없기 때문입니다.
• 만약에 800원을 거슬러 주어야 하는데 화평 단위가 500원, 400원, 100원이라면 어떻게 될까요?
• 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검
토할 수 있어야 합니다.
'''


n = 1260
count = 0

array=[500, 100, 50, 10]

for coin in array:
    count += n // coin # 몫
    n %= coin # 나머지
    
print(count)