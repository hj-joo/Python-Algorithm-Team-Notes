'''
• 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 
예를 들어 1을 입력했을 때 다음은 30 하나라도 포함되 어 있으므로 세어야 하는 시각입니다.

• 00시 00분 03초
• 00시 13분 30초

• 반면에 다음은 30 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
• 00시 02분 55초
• 01시 27분 45초
''' 

'''
N = 5
00시 00분 00초
~
05시 59분 59초 
'''

clock = int(input())
count = 0
for hour in range(clock+1):
    for minute in range(60):
        for second in range(60):
            # 문자열로 바꾼 후 3이 포함되어 있으면 됨
            if '3' in str(hour) + str(minute) + str(second):
                count +=1
                    
print(count)