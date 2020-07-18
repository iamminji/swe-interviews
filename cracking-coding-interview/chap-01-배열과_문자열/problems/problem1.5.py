"""
1.5
문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제, 문자 교체.
문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라.
"""


def edit_string(s1, s2):
    i, j = 0, 0
    count = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            continue

        count += 1

        if count > 1:
            return False

        if len(s1) > len(s2):
            i += 1
        elif len(s1) < len(s2):
            j += 1
        else:
            i += 1
            j += 1

    return True


if __name__ == '__main__':
    assert edit_string("pale", "ple") is True
    assert edit_string("pales", "pale") is True
    assert edit_string("pale", "bale") is True
    assert edit_string("pale", "bake") is False
    assert edit_string("palekp", "palegk") is False
