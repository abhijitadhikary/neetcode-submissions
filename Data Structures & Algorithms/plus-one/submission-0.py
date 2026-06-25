class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        carry = 1
        list_ret = [0]
        for idx in range(len(digits)-2, -1, -1):
            sum_c = digits[idx] + carry
            carry = sum_c // 10
            list_ret.append(sum_c % 10)
        if carry > 0:
            list_ret.append(carry)
        return list_ret[::-1]