import sys

class StringMultiply:
    def __init__(self):
        self.numArr = []
    #did not pass all test cases, the int value exceeding the limit
    def multiply(self, num1, num2):
        for index1, char1 in enumerate(num2[::-1]):
            tensPlace = 0
            rem = ""
            for index, char2 in enumerate(num1[::-1]):
                #print(str(index) + "   " + str(char1) + str(char2))
                res = (int(char1) * int(char2)) + int(tensPlace)

                if index+1 == len(num1):
                    rem = str(res) + rem
                    tensPlace = 0
                elif res >= 10:
                    rem = str(res % 10) + rem
                    tensPlace = int(res / 10)
                else:
                    rem = str(res) + rem
                    tensPlace = 0
                #print(10 ** index)
                #rem = str(int(rem) * (10 ** index))
                #print(str(res) + "   " + str(tensPlace) + "    " + rem)
            self.numArr.append(str(int(rem) * (10 ** index1)))
            #print(rem)
        print(self.numArr)
    #simple solution - passed all test cases on leetcode
    def multiply1(self, num1, num2):
        res = 0
        num1, num2 = num1[::-1], num2[::-1]
        for i1, d1 in enumerate(num1):
            for i2, d2 in enumerate(num2):
                res += (ord(d1) - ord('0')) * (ord(d2) - ord('0')) * 10**(i1+i2)
                #print(str(d1) + "   " + str(ord(d1) - ord('0')) + "   " + str(d2) + "   " + str(ord(d2) - ord('0')))
        return str(res)
    def multiply2(self, num1, num2):
        res = 0
        num1, num2 = num1[::-1], num2[::-1]
        for i1, d1 in enumerate(num1):
            for i2, d2 in enumerate(num2):
                res += (int(d1)) * (int(d2)) * 10**(i1+i2)
        return str(res)
        

if __name__ == "__main__":
    sm = StringMultiply()
    print(sm.multiply2("123456789", "987654321"))
    #sm.multiply("123456789", "3")