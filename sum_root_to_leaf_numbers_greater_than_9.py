from typing import Optional
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

        #in order to splice two ints together we need to know how many decimals places
        #to move prev over before adding node val to it
        #we can use a temp value to divide node val by 10 until we get 0 with truncation
        #if we had three numbers we want to multiply by by 1000 to move over three to fit the next three
        #200, 123 multiply 200 by 1000 then add 123 to it
        # 0 is an edge case where we have to hardcode set it to 1 instead of 10

def sumNumbers(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node, prev):
        if not node:
            return
        nonlocal res
        node_val = node.val
        digits = 10 if node.val == 0 else 1
        while node_val > 0:
            digits *= 10
            node_val //= 10
        sumVal = (prev * digits) + node.val
        if not node.left and not node.right:
            res += sumVal
        dfs(node.left, sumVal)
        dfs(node.right, sumVal)
    dfs(root, 0)
    return res

def test_sum_numbers():
    root = TreeNode(10)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    result = sumNumbers(root)
    expected = (100 + 100)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

    root = TreeNode(220)
    root.left = TreeNode(123)
    result = sumNumbers(root)
    expected = (220123)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(912)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(4)
    root.right = TreeNode(46)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(61)
    result = sumNumbers(root)
    expected = (129123 + 129124  + 1465 + 14661)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(912)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(4)
    root.right = TreeNode(46)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(61)
    result = sumNumbers(root)
    expected = (129123 + 129124 + 1465 + 14661)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

    root = TreeNode(10)
    root.left = TreeNode(200)
    root.right = TreeNode(300)
    result = sumNumbers(root)
    expected = (10200 + 10300)
    assert expected == result, f"Test case failed: expected {expected}, got {result}"
    print(f"Test case passed: {result}")

if __name__ == '__main__':
    test_sum_numbers()