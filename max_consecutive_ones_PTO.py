from typing import List


def maxConsecutiveOnesPTO(days: List[str], pto: int) -> int:
    res = l = vacation = 0
    for r in range(len(days)):
        if days[r] == "W":
            vacation += 1
        while vacation > pto:
            if days[l] == "W":
                vacation -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

def test():
    test_cases = [
        (['W', 'H', 'H', 'W', 'W', 'H', 'W'], 2, 5),
        (['W', 'W', 'H', 'H', 'W', 'W', 'W'],0, 2),
        (['W', 'W', 'H', 'H', 'W', 'W', 'W'], 5, 7),
        (['W', 'W', 'H', 'H', 'W', 'W', 'W'], 10, 7),
        (['H', 'H', 'H', 'H', 'H', 'H', 'H'], 0, 7),
        (['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H'], 1, 3),
    ]

    for i, (days, pto, expected_output) in enumerate(test_cases):
        result = maxConsecutiveOnesPTO(days, pto)
        assert result == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {result}"

    print("All test cases passed!")
if __name__ == '__main__':
    test()