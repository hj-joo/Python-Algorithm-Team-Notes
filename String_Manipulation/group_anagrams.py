'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

•입력
["eat", "tea", "tan", "ate", "nat", "bat"]

•출력
[
["ate","eat","tea"], ["nat", "tan"], ["bat"]
]
'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = dict()
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
            
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))