# This is a sample Python script.
import random
from typing import List

def reservoir(nums:List[int], k: int) -> List[int]:
    res = [0] * k
    for i in range(k):
        res[i] = nums[i]
    for i in range(k, len(nums)):
        rand = random.randint(0, i)
        if rand < k:
            res[rand] = nums[i]
    return res


def test_reservoir():
    # Set a seed for reproducibility
    random.seed(42)

    # Test case 1: k = 1 (select one element)
    nums1 = [1, 2, 3, 4, 5]
    result1 = reservoir(nums1, 1)
    assert len(result1) == 1
    assert result1[0] in nums1

    # Test case 2: k = 3 (select three elements)
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result2 = reservoir(nums2, 3)
    assert len(result2) == 3
    assert all(num in nums2 for num in result2)

    # Test case 3: k = len(nums) (select all elements)
    nums3 = [10, 20, 30, 40, 50]
    result3 = reservoir(nums3, len(nums3))
    assert len(result3) == len(nums3)
    assert sorted(result3) == sorted(nums3)

    # Test case 4: k = 0 (select no elements)
    nums4 = [1, 2, 3, 4, 5]
    result4 = reservoir(nums4, 0)
    assert len(result4) == 0


    # Test case 7: All elements are the same
    nums7 = [7, 7, 7, 7, 7]
    result7 = reservoir(nums7, 2)
    assert len(result7) == 2
    assert all(num == 7 for num in result7)

    print("All test cases passed!")


if __name__ == "__main__":
    test_reservoir()
