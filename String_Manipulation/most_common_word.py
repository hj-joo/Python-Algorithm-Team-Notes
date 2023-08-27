'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
• 입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

• 출력
"ball"

'''
import re
from collections import Counter
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    # 모든 단어를 소문자로 변환하고, 알파벳과 숫자가 아닌 문자는 공백으로 대체
    words = re.sub('[^\w]', ' ', paragraph.lower()).split()

    # banned 단어 리스트도 소문자로 변환.
    banned = set(word.lower() for word in banned)
    
    # banned 단어 리스트에 없는 단어만 new_paragraph 리스트에 추가
    new_paragraph = [word for word in words if word not in banned]

    counts = Counter(new_paragraph)
    return counts.most_common(1)[0][0]


print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
            