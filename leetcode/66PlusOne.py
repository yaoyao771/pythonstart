
'''Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        flag = 1
        for i in range(length - 1, -1, -1):
            digits[i] += flag
            if digits[i] > 9:
                flag = 1
                digits[i] = digits[i] % 10
            else:
                flag = 0
        if flag == 1:
            digits.insert(0, 1)
        return digits
