"""
1.3
문자열에 들어 있 모든 공백을 '%20' 으로 바꿔 주는 메서드를 작성하라.
최종적으로 모든 문자를 다 담을 수 있을 만큼 충분한 공간이 이미 확보되어 있으며 문자열의 최종 길이가 함께 주어진다고 가정해도 된다.
"""


# length 의 경우 python 을 사용할 때 안 써도 되서 안 썼다.(?)
def encode_only_white_space(s, length):
    l = list()
    for c in s:
        if c == " ":
            l.append("%20")
        else:
            l.append(c)

    return "".join(l)


if __name__ == '__main__':
    s = "Mr john Smith"
    l = 13
    print(encode_only_white_space(s, l))
