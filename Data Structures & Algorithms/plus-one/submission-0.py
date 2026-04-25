class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []

        added = digits[-1] + 1 
        leftover = added % 10
        carry = added // 10
        res.append(leftover)
        print(res)

        for i in range(len(digits)-2, -1, -1):
            print(carry)
            digit_sum = digits[i] + carry
            leftover = digit_sum % 10
            carry = digit_sum // 10
            res.append(leftover) 
            print(res)

        if carry != 0:
            res.append(carry)

        return res[::-1]
            