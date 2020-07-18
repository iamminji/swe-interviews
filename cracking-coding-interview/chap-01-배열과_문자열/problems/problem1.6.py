"""
1.6
반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
만약 "압축된" 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다.
문자열은 대소문자 알파벳으로만 이루어져있다.
"""


def compress_str(s):
    prev = s[0]
    l = list()
    c = 1
    for i in range(1, len(s)):
        if prev == s[i]:
            c += 1
        else:
            l.append(prev)
            l.append(str(c))
            c = 1
        prev = s[i]

    l.append(prev)
    l.append(str(c))

    if len(l) > len(s):
        return s
    return "".join(l)


if __name__ == '__main__':
    assert compress_str("aabccccaaa") == "a2b1c4a3"
    assert compress_str("avcccddefggggggg") == "a1v1c3d2e1f1g7"
    assert compress_str("abcdef") == "abcdef"
