"""
1.8
MXN 행렬의 한 원소가 0일 경우, 해당 원솨 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.
"""


def replace_zero(m):
    keep = dict()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                keep[(i, j)] = True

    for x, y in keep:
        m[x] = [0 for _ in range(len(m[x]))]
        for j in range(len(m)):
            m[j][y] = 0

    return m


if __name__ == '__main__':
    m = [[1, 2, 0], [2, 3, 4]]
    assert replace_zero(m) == [[0, 0, 0], [2, 3, 0]]
    m2 = [[1, 2, 0, 4], [2, 3, 4, 5]]
    assert replace_zero(m2) == [[0, 0, 0, 0], [2, 3, 0, 5]]
