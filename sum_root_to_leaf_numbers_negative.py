from typing import Optional
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node, prev, numNeg):
        if not node:
            return None
        nonlocal res
        sumVal = prev * 10 + abs(node.val)
        if node.val < 0:
            numNeg += 1
        if not node.left and not node.right:
            if numNeg % 2 != 0:
                sumVal *= -1
            res += sumVal
        dfs(node.left, sumVal, numNeg)
        dfs(node.right, sumVal, numNeg)
    dfs(root, 0, 0)
    return res

def test_sum_numbers():
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.left.left = TreeNode(-9)
    root.right = TreeNode(4)
    root.right.left = TreeNode(-5)
    result = sumNumbers(root)
    expected = (-129 + 145)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.left.left = TreeNode(-9)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(-5)
    root.right.right = TreeNode(6)

    result = sumNumbers(root)
    expected = (-1293 + 1293 + 145 + -146)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

    assert 0 == sumNumbers(None)

if __name__ == '__main__':
    test_sum_numbers()