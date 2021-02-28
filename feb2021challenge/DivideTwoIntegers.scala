object DivideTwoIntegers {
/*
Divide two integers
----------------------
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

*/

  def divide(dividend: Int, divisor: Int): Int = {
        if(dividend == 0) {
            return 0
        }

        var posDivd: Long = dividend
        var posDivr: Long = divisor
        var divdSign = true
        var divrSign = true

        if(dividend < 0) {
            posDivd = -posDivd
            if(posDivd < 0) {
                posDivd = Integer.MAX_VALUE
            }
            divdSign = false
        }

        if(divisor < 0) {
            posDivr = -posDivr
            if(posDivr < 0) {
                posDivr = Integer.MAX_VALUE
            }
            divrSign = false
        }

        if(posDivr == 1) {
            if(divdSign == divrSign) {
                return Math.min(posDivd, Integer.MAX_VALUE).toInt
            } else {
                return Math.max(-posDivd, Integer.MIN_VALUE).toInt
            }
        }

        var temp:Long = posDivr
        var count:Long = 0
        while(temp <= posDivd) {
            temp += posDivr
            count+=1
        }

        if(divdSign == divrSign) {
            return Math.min(count, Integer.MAX_VALUE).toInt
        } else {
            return Math.max(-count, Integer.MIN_VALUE).toInt
        }
  }

  def main(args: Array[String]): Unit = {
    //println(divide(7, -3))
    //println(divide(Math.pow(2, 32).toInt, 1))
    //println(divide(-1, 1))
    println(divide(-2147483648, 2)) //-1073741824
    //println(divide(1, -1))
  }
}
