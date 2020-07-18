"""
1.1
문자열이 부어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라.
자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.
"""


# 자료구조를 사용해서 중복을 판단하는 방법
# Map(dict) 사용
def has_duplicates_01(s):
    from collections import Counter
    counter = Counter(s)
    for k in counter:
        if counter[k] == 2:
            return True
    return False


# 자료구조를 사용해서 중복을 판단하는 방법
# Set 사용
def has_duplicates_02(s):
    set_ = set()

    for c in s:
        if c in set_:
            return True
        set_.add(c)
    return False


# 자료구조를 사용하지 않고 중복을 판단하는 방법
# 2중 for-loop
def has_duplicates_03(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return True

    return False


if __name__ == '__main__':
    s = "abcdefga"
    print(has_duplicates_01(s))
    print(has_duplicates_02(s))
    print(has_duplicates_03(s))
