class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry

            bit = total % 2
            carry = total // 2
            result.append(str(bit))
            i -=1
            j-=1
            
        return "".join(result[::-1])



