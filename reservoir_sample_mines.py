import random
from typing import List, Tuple


def generate_mines(m: int, n: int, k: int) -> List[Tuple[int, int]]:
    """
    Generates k mines randomly on an m x n grid using Reservoir Sampling.
    Each cell has an equal probability of being chosen.
    """
    if k <= 0 or m <= 0 or n <= 0 or k > m * n:
        return []  # Edge cases
    res = []
    for i in range(k):
        r = i // n
        c = i % n
        res.append((r,c))
    for i in range(k, m * n):
        rand = random.randint(0, i)
        if rand < k:
            r = i // n
            c = i % n
            res[rand] = (r,c)
    return res

def test_generate_mines():
    # Test case 1: Small grid, k = 1
    m, n, k = 2, 2, 1
    mines = generate_mines(m, n, k)
    assert len(mines) == k
    assert all(0 <= mine[0] < m and 0 <= mine[1] < n for mine in mines)

    # Test case 2: Larger grid, k = 5
    m, n, k = 5, 5, 5
    mines = generate_mines(m, n, k)
    assert len(mines) == k
    assert len(set(mines)) == k

    # Test case 3: k = m * n (all cells are mines)
    m, n, k = 3, 3, 9
    mines = generate_mines(m, n, k)
    assert len(mines) == k
    assert len(set(mines)) == k

    # Test case 4: k = 0 (no mines)
    m, n, k = 4, 4, 0
    mines = generate_mines(m, n, k)
    assert len(mines) == 0

    # Test case 5: k > m * n (invalid input)
    m, n, k = 2, 2, 5
    mines = generate_mines(m, n, k)
    assert len(mines) == 0

    # Statistical test
    m, n, k = 10, 10, 10
    cell_counts = [[0 for _ in range(n)] for _ in range(m)]
    num_trials = 20000
    for _ in range(num_trials):
        mines = generate_mines(m, n, k)
        for mine in mines:
            cell_counts[mine[0]][mine[1]] += 1

    expected_count = (k / (m * n)) * num_trials
    tolerance = 0.1 * expected_count
    for row in range(m):
        for col in range(n):
            assert abs(cell_counts[row][col] - expected_count) <= tolerance

    print("All test cases passed!")

if __name__ == "__main__":
    test_generate_mines()

    # Example usage
    m, n, k = 5, 5, 5
    mines = generate_mines(m, n, k)
    print(f"Mines on a {m}x{n} grid: {mines}")