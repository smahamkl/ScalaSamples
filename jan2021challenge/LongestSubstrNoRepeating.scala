import scala.collection.mutable.HashMap
import scala.math
/*
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
*/
object Solution{
    def lengthOfLongestSubstring(s: String): Int = {
        if(s.length() == 0)
            return 0

        val chMap:HashMap[Char, Int] = HashMap()
        var left = 0
        var right = 0
        var res = 0
        while(right < s.length()){
            if(!chMap.contains(s(right))){
                chMap += s(right)->1
                res = math.max(res, right-left+1)
                right += 1
            }else{
                chMap.remove(s(left))
                left += 1            
            }
        }

        res
    }

    def main(args: Array[String]):Unit = {
        println(lengthOfLongestSubstring("abcabcbb"))
        println(lengthOfLongestSubstring("bbbbbb"))
        println(lengthOfLongestSubstring("pwwkew"))
        println(lengthOfLongestSubstring("aba"))
        println(lengthOfLongestSubstring("a"))
        println(lengthOfLongestSubstring("au"))
        println(lengthOfLongestSubstring(""))
        println(lengthOfLongestSubstring("dvdf"))
    }
}