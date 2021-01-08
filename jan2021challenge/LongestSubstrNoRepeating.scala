import scala.collection.mutable.HashSet

object Solution{
    def lengthOfLongestSubstring(s: String): Int = {

        if(s.length() == 0)
            return 0

        var res:String = s.charAt(0).toString()
        val charMap:HashSet[Char] = HashSet()
        charMap.add(s.charAt(0))
        var curCh:Int = 0

        for(i<-1 to s.length()-1)
        {
            if(charMap.contains(s.charAt(i))){
                if((i - curCh) > res.length()){
                    res = s.substring(curCh, i)
                }
                charMap.clear()
                charMap.add(s.charAt(i))
                curCh = i
            }else if(i == (s.length() - 1)){
                if((i - curCh + 1) > res.length()){
                    res = s.substring(curCh, i+1)
                }
            }
            charMap.add(s.charAt(i))
        }
        println(res)
        res.length()
        
    }

    def main(args: Array[String]):Unit = {
        // println(lengthOfLongestSubstring("abcabcbb"))
        // println(lengthOfLongestSubstring("bbbbbb"))
        // println(lengthOfLongestSubstring("pwwkew"))
        // println(lengthOfLongestSubstring("aba"))
        // println(lengthOfLongestSubstring("a"))
        // println(lengthOfLongestSubstring("au"))
        // println(lengthOfLongestSubstring(""))
        println(lengthOfLongestSubstring("dvdf"))
    }
}