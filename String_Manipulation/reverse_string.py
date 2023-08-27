def reverseString(s: list[str]) -> list[str]:
    # Two pointer
    left, right = 0, len(s) - 1
    # print(left, right)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
    # python 
    #s.reverse()
    
print(reverseString(["h","e","l","l","o"])) 