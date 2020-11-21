class Solution:
    def sumStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
    
    def addStrings(self, num1:str, num2: str) -> str:
        if not num1 and not num2:
            return "0"
        elif not num1:
            return num2
        elif not num2:
            return num1

        if '.' in num1:
            n1arr = num1.split(".")
        else:
            n1arr = [num1, "0"]
        
        if '.' in num2:
            n2arr = num2.split(".")
        else:
            n2arr = [num2, "0"]
        
        if len(n1arr[1]) > len(n2arr[1]):
            n2arr[1] = n2arr[1].ljust(len(n1arr[1]), '0')
        elif len(n2arr[1]) > len(n1arr[1]):
            n1arr[1] = n1arr[1].ljust(len(n2arr[1]), '0')
        
        decsum = self.sumStrings(n1arr[1], n2arr[1])

        decsum, dec_car = decsum[len(decsum)-len(n1arr[1]):], decsum[:len(decsum)-len(n1arr[1])]
        sum = self.sumStrings(dec_car, n1arr[0])
        sum = self.sumStrings(sum, n2arr[0]) + "." + decsum
        return sum


sol = Solution()
print(sol.addStrings("9", "1"))