# This is a sample Python script.
from typing import List

def findUnique(nums:List[int]) -> int:
    uniques = 0
    i = 0
    while i < len(nums):
        uniques += 1
        l, r = i, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == nums[i]:
                l = mid + 1
            else:
                r = mid - 1
        i = l
    return uniques

if __name__ == "__main__":
    num = [5,5,5,5,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9]
    assert findUnique(num) == 4

    num = [5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 11]
    assert findUnique(num) == 6

    num = [5]
    assert findUnique(num) == 1

    print("all tests passed!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
