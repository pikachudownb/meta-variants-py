from typing import List

def tryMerge(res, curr):
    if not res:
        res.append(curr)
    else:
        prev = res[-1]
        if prev[1] >= curr[0]:
            prev[0] = min(prev[0], curr[0])
            prev[1] = max(prev[1], curr[1])
        else:
            res.append(curr)

def merge_2_interval_lists_56_variant_python(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    a = b = 0
    res = []
    while a < len(A) and b < len(B):
        if A[a][0] < B[b][0]:
            tryMerge(res,A[a])
            a += 1
        else:
            tryMerge(res, B[b])
            b += 1
    while a < len(A):
        tryMerge(res, A[a])
        a += 1
    while b < len(B):
        tryMerge(res, B[b])
        b += 1
    return res

if __name__ == "__main__":
    A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
    B = [[2, 8], [13, 20]]
    expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
    actual = merge_2_interval_lists_56_variant_python(A, B)
    assert expected == actual

    A = []
    B = [[2, 8], [13, 20]]
    expected = [[2, 8], [13, 20]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [10, 15], [20, 25]]
    B = [[5, 10], [15, 20]]
    expected = [[1, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)

    A = [[1, 5], [11, 15], [21, 25]]
    B = [[6, 10], [16, 20]]
    expected = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]
    assert expected == merge_2_interval_lists_56_variant_python(A, B)