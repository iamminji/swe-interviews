"""
1.9
한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring 이라는 메서드가 있다고 하자.
s1과 s2의 두 문자열이 주어졌고, s2가 s1을 회전 시킨 결과인지 판별하고자 한다.
isSubstring 메서드를 한 번만 호출해서 판별할 수 있는 코드를 작성하라.
"""


def is_sub_string(s1, s2):
    return True if s2 in s1 else False


def can_generate_str_only_once_rotate(s1, s2):
    return is_sub_string(s1 + s1, s2)


if __name__ == '__main__':
    assert can_generate_str_only_once_rotate("waterbottle", "erbottlewat")
