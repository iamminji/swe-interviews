"""
1.2
문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는 확인하는 메서드를 작성하라
"""


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    from collections import Counter
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    for k1 in counter1:
        if k1 not in counter2:
            return False
        if counter1[k1] != counter2[k1]:
            return False

    for k2 in counter2:
        if k2 not in counter1:
            return False
        if counter2[k2] != counter1[k2]:
            return False

    return True


if __name__ == '__main__':
    print(is_permutation("abckgg", "kbcagg"))
    print(is_permutation("abcd", "bca"))
    print(is_permutation("abcdh", "dbcag"))
