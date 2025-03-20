import random
from typing import List, Tuple

class Solution:
    def __init__(self, cities: List[Tuple[str,int]]) -> None:
        self.prefix = [cities[0]]
        for i in range(1, len(cities)):
            name, pop = cities[i]
            self.prefix.append((name, self.prefix[-1][1] + pop))
    def pick(self)-> str:
        rand = random.randint(0, self.prefix[-1][1] - 1)
        l, r = 0, len(self.prefix) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.prefix[mid][1] > rand:
                r = mid - 1
            else:
                l = mid + 1
        return self.prefix[l][0]

def test():
    # Define test cases as a list of tuples: (cwd, cd, expected_output)
    test_cases = [
        (42, [("seattle", 500),("NY", 900),("LA", 400)], "NY"),
        (2421, [("seattle", 500), ("NY", 900), ("LA", 400)], "seattle"),
        (13, [("seattle", 500), ("NY", 900), ("LA", 400)], "NY"),
        (2, [("seattle", 500), ("NY", 900), ("LA", 400)], "LA"),
    ]
    # Run through each test case and assert the result
    for i, (seed, cities, expected) in enumerate(test_cases):
        random.seed(seed)
        solution = Solution(cities)
        result = solution.pick()
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: {result}")

if __name__ == '__main__':
    test()
