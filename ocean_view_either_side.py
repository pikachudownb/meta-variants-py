from typing import List


def oceanViews(build: List[int]) -> List[int]:
    if len(build) == 1:
        return [0]
    maxLeft = maxRight = 0
    lViews, rViews = [], []
    l, r = 0, len(build) - 1
    while l < r:
        if build[l] > maxLeft:
            maxLeft = build[l]
            lViews.append(l)
        if build[r] > maxRight:
            maxRight = build[r]
            rViews.append(r)
        if build[l] < build[r]:
            l += 1
        else:
            r -= 1
    rViews.reverse()
    lViews.extend(rViews)
    return lViews


def test_ocean_views():
    # Define test cases as a list of tuples: (cwd, cd, expected_output)
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 2],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, 2, 3, 3, 2, 1],[0,1,2,3,4,5]),
        ([1, 4, 3, 9, 8, 6],[0,1,3,4,5]),
        ([1, 2, 1, 1, 3, 1, 1, 3, 1, 3, 2, 1],[0,1,4,9,10,11]),
        ([1,1,1,1],[0,3]),
        ([5],[0]),
        ([1,10],[0,1])
    ]

    # Run through each test case and assert the result
    for i, (buildings, expected) in enumerate(test_cases):
        result = oceanViews(buildings)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: {result}")

if __name__ == '__main__':
    test_ocean_views()
