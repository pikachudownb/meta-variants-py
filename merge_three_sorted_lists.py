from typing import List


def merge_3_sorted_lists_first_variant_21_python(listA: List[int],
                                                 listB: List[int],
                                                 listC: List[int]) -> List[int]:
    res = []
    a = b = c = 0
    while a < len(listA) or b < len(listB) or c < len(listC):
        aVal = listA[a] if a < len(listA) else float("inf")
        bVal = listB[b] if b < len(listB) else float("inf")
        cVal = listC[c] if c < len(listC) else float("inf")
        minVal = min(aVal, bVal, cVal)
        res.append(minVal)
        if minVal == aVal:
            a += 1
        elif minVal == bVal:
            b += 1
        else:
            c += 1
    return res

if __name__ == '__main__':
    a = [1, 1, 1, 3, 4, 5]
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 8, 8, 10]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = []
    b = [3, 3, 4, 5, 6]
    c = [1, 1, 3, 3, 8, 8, 8, 10]
    expected = [1, 1, 3, 3, 3, 3, 4, 5, 6, 8, 8, 8, 10]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = []
    b = []
    c = []
    expected = []
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [1]
    b = [2]
    c = [3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]
    expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)

    a = [2, 2]
    b = [2]
    c = [0]
    expected = [0, 2, 2, 2]
    assert expected == merge_3_sorted_lists_first_variant_21_python(a, b, c)
    print("all tests passed!")