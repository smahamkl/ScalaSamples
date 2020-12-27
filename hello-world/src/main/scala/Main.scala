/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
*/
object Solution {

  def numDecodings(s: String): Int = {
    if (s.slice(0, 1).toInt == 0) 0
    else {
      // says how many ways you can decode a string of a given length
      val waysToDecode: Array[Int] = Array.fill(s.length + 1)(0)

      // assume empty string has one way to encode
      waysToDecode(0) = 1
      // we know the string doesn't started with "0", since we've checked that case above
      // therefore the first number is always decodable, and there is always one way to decode it
      waysToDecode(1) = 1
      for (l <- 2 to s.length) {
        val singleDigit = s.slice(l - 1, l).toInt
        val doubleDigit = s.slice(l - 2, l).toInt

        val isSingleValid = 1 <= singleDigit
        val isDoubleValid = 10 <= doubleDigit && doubleDigit <= 26

        if (isSingleValid) waysToDecode(l) += waysToDecode(l - 1)
        if (isDoubleValid) waysToDecode(l) += waysToDecode(l - 2)
      }

      waysToDecode(s.length)
    }
  }

  def main(args: Array[String]) {
    // println(numDecodings("11101"))
    // println(numDecodings("2101"))
    // println(numDecodings("226"))
    // println(numDecodings("12"))
    // println(numDecodings("1111"))
    // println(numDecodings("1"))
    // println(numDecodings("127"))
    // println(numDecodings("0"))
    // println(numDecodings("00"))
    // println(numDecodings("626"))
    // println(numDecodings("10"))
    println(numDecodings("1123")) //5
  }
}
