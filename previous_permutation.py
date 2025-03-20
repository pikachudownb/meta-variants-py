from typing import Optional, List


def previousPermutation(nums: List[int]) -> List[int]:
    pivot = None
    for i in range(len(nums) - 1, 0, -1):
        curr = nums[i]
        next = nums[i - 1]
        if next > curr:
            pivot = i - 1
            break
    if pivot == None:
        nums.reverse()
        return nums
    swap = len(nums) - 1
    while nums[swap] >= nums[pivot]:
        swap -= 1
    nums[swap], nums[pivot] = nums[pivot], nums[swap]
    l, r = pivot + 1, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


def test_prev_perm():
    test_cases = [
        ([9,4,8,3,5,5,8,9],[9,4,5,9,8,8,5,3])
    ]

    for i, (input_nums, expected_output) in enumerate(test_cases):
        result = previousPermutation(input_nums)
        assert result == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {result}"

    print("All test cases passed!")
if __name__ == '__main__':
    test_prev_perm()