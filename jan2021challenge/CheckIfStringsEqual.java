package jan2021challenge;
/*
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
*/
public class CheckIfStringsEqual {

    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int l1 = word1.length;
        int l2 = word2.length;

        String res1 = "", res2 = "";

        for(int i=0;i<Math.max(l1, l2);i++)
        {
            res1+= i < l1 ? word1[i] : "";
            res2+= i < l2 ? word2[i] : "";
        }
        return res1.equals(res2);
    }

    public static void main(String[] args)
    {
        System.out.println(new CheckIfStringsEqual().arrayStringsAreEqual(new String[]{"ab", "c"}, new String[]{"a", "b", "c"}));
        System.out.println(new CheckIfStringsEqual().arrayStringsAreEqual(new String[]{"a", "cb"}, new String[]{"abc"}));
        System.out.println(new CheckIfStringsEqual().arrayStringsAreEqual(new String[]{"abc", "d", "defg"}, new String[]{"abcddefg"}));
    }
    
}
