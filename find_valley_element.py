# This is a sample Python script.
from typing import List


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def findValleyElement(nums:List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        lBound = nums[mid - 1] if mid != 0 else float("inf")
        rBound = nums[mid + 1] if mid != len(nums) - 1 else float("inf")
        if lBound > nums[mid] < rBound:
            return mid
        if nums[mid] > rBound:
            l = mid + 1
        else:
            r = mid - 1
    return -1 #unreachable


if __name__ == "__main__":
    num = [3, 2, 3, 4, 3, 2]
    assert findValleyElement(num) == 1

    num = [1, 2, 3, 1]
    assert findValleyElement(num) == 0

    num = [1, 2, 3, 5, 3, 4, 3, 1, 6]
    assert findValleyElement(num) == 4

    num = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(num) == 0

    num = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(num) == 0

    num = [1, 2, 3, 2, 1, 0]
    assert findValleyElement(num) == 5  # Right pos infinity yields valley

    num = [1, 2, 3, 2, 1, 6]
    assert findValleyElement(num) == 4

    num = [9,8,7,6,5,4,5,6,7,8,9]
    assert findValleyElement(num) == 5

    print("all tests passed!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
