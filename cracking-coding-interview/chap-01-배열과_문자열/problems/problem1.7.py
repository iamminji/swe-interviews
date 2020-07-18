"""
1.7
이미지를 표현하는 NXN 행렬이 있다. 이미지의 각 픽셀은 4바이트로 표현된다.
이때, 이미지를 90도 회전 시키는 메서드를 작성하라.
행렬을 추가로 사용하지 않고서도 할 수 있겠는가?
"""

"""
비슷한 문제
https://leetcode.com/problems/rotate-image/
"""


# use memory
def rotate_matrix_01(m):
    res = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            res[j][len(m) - i - 1] = m[i][j]

    return res


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_matrix_01(m) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    m2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    assert rotate_matrix_01(m2) == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
