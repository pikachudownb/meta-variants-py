# This is a sample Python script.
from typing import List


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def simplifyPath(cwd, cd) -> str:
    if not cd:
        return cwd
    stack = []
    if cd[0] != "/":
        for path in cwd.split("/"):
            if path not in ["","/"]:
                stack.append(path)
    for path in cd.split("/"):
        if path in ["",".","/"]:
            continue
        if stack and path == "..":
            stack.pop()
        if path != "..":
            stack.append(path)
    res = ["/"]
    for i, path in enumerate(stack):
        res.append(path)
        if i != len(stack) - 1:
            res.append("/")
    return "".join(res)

def test_simplifyPath():
    # Define test cases as a list of tuples: (cwd, cd, expected_output)
    test_cases = [
        ("/", "foo", "/foo"),
        ("/","foo/bar/././xyz///","/foo/bar/xyz"),
        ("/baz", "/bar", "/bar"),
        ("/foo/bar", "../../../../..","/"),
        ("/x/y","../p/../q", "/x/q"),
        ("/x/y","/p/./q","/p/q"),
        ("/facebook/anin", "../abc/def", "/facebook/abc/def"),
        ("/facebook/instagram", "../../../../.", "/")
    ]

    # Run through each test case and assert the result
    for i, (cwd, cd, expected) in enumerate(test_cases):
        result = simplifyPath(cwd, cd)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: {result}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_simplifyPath()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
