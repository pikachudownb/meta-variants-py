import random
from typing import List


def random_pick_index_max(nums: List[int]) -> int:
    maxNum = float("-inf")
    candidate = -1
    count = 1
    for i, num in enumerate(nums):
        if num > maxNum:
            count = 1
            maxNum = num
            candidate = i
        if num == maxNum:
            rand = random.randint(1, count)
            if rand == 1:
                candidate = i
            count += 1
    return candidate

def test_random_pick_index_max():
    nums1 = [1, 2, 3, 4, 5]
    assert random_pick_index_max(nums1) == 4

    nums2 = [1, 3, 2, 3, 3]
    # Run the function multiple times to see if it picks different indices
    indices = set()
    for _ in range(1000):
        indices.add(random_pick_index_max(nums2))
    assert indices == {1, 3, 4}

    nums3 = [7, 7, 7, 7]
    indices = set()
    for _ in range(1000):
        indices.add(random_pick_index_max(nums3))
    assert indices == {0, 1, 2, 3}

    nums4 = []
    assert random_pick_index_max(nums4) == -1

    nums5 = [42]
    assert random_pick_index_max(nums5) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_random_pick_index_max()