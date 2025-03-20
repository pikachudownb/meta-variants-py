from typing import List
def addStrings(num1: str, num2: str, carry: int):
    a = len(num1) - 1
    b = len(num2) - 1
    sb = []
    while a >= 0 or b >= 0:
        sumVal = carry
        if a >= 0:
            sumVal += ord(num1[a]) - ord("0")
        if b >= 0:
            sumVal += ord(num2[b]) - ord("0")
        digit = str(sumVal % 10)
        carry = sumVal // 10
        sb.append(digit)
        a -= 1
        b -= 1
    sb.reverse()
    return "".join(sb), carry

def addDecimalStrings(num1:str, num2:str) -> str:
    nums1 = num1.split(".")
    nums2 = num2.split(".")
    decimals1 = nums1[1] if len(nums1) == 2 else ""
    decimals2 = nums2[1] if len(nums2) == 2 else ""
    hasDecimals = decimals1 or decimals2
    while len(decimals1) != len(decimals2):
        if len(decimals1) < len(decimals2):
            decimals1 += "0"
        else:
            decimals2 += "0"
    result = []
    decStr, carry = addStrings(decimals1, decimals2, 0)
    result.append(decStr)
    if hasDecimals:
        result.append(".")
    numStr, carry = addStrings(nums1[0], nums2[0], carry)
    result.append(numStr)
    if carry == 1:
        result.append("1")
    result.reverse()
    return "".join(result)



def test():
    actual = addDecimalStrings("91.465", "72.8")
    assert actual == "164.265"

    actual = addDecimalStrings("20", "4")
    assert  actual == "24"
    print("all tests passed!")



if __name__ == '__main__':
   test()
