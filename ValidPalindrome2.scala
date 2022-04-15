object ValidPalindrome2 extends App{

/*
LeetCode 680
Valid Palindrome 2
Given a string s, return true if the s can be palindrome after deleting at most one character from it
*/
  def checkIfSameChars(s: String, l: Int, r: Int, totalMisMatches:Int): Boolean = {
    if(l >= r && totalMisMatches <= 1)
      return true
    else if(totalMisMatches > 1)
      return false
    
    if(s(l) == s(r))
      return checkIfSameChars(s, l+1, r-1, totalMisMatches)
    else
      return checkIfSameChars(s, l+1, r, totalMisMatches+1) || checkIfSameChars(s, l, r-1, totalMisMatches+1)
  }
  def validPalindrome(s: String): Boolean = {
    return checkIfSameChars(s, 0, s.length-1, 0)
  }

  println(validPalindrome(("abc")))
  println(validPalindrome(("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")))

}