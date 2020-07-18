"""
1.4
주어진 문자열이 회문의 순열인지 아닌지 확인하는 함수를 작성하라.
회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치하는 것을 뜻한다.
회문이 꼭 사전에 등장하는 단어로 제한될 필요는 없다.
"""


def can_be_palindrome(s):
    s = s.lower()
    # 회문이 되기 위해선 문자열의 길이가 짝수일 때
    # 홀수개의 문자가 등장하면 안된다.
    # 공백은 무시한다.

    from collections import Counter
    counter = Counter()
    length = 0
    for c in s:
        if c != " ":
            counter[c] += 1
            length += 1

    for k in counter:
        # 문자열이 짝수일 때
        if length % 2 == 0:
            if counter[k] % 2 == 1:
                return False

    return True


if __name__ == '__main__':
    print(can_be_palindrome("Tact Coa"))
    print(can_be_palindrome("ABAC"))
    print(can_be_palindrome("ABAB"))
    print(can_be_palindrome("ccca"))
    print(can_be_palindrome("ccacc"))
    print(can_be_palindrome("hellohello"))
