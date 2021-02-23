package feb2021challenge;

import java.util.List;
import java.util.Arrays;

/*

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
*/

public class LongestWordDict {

    public int compareStrings(String s1, String s2)
    {
        int tot = 0;
        int i = 0, j = 0;
        while(i< s1.length() && j < s2.length())
        {
            if(s1.charAt(i) == s2.charAt(j))
            {
                i++;
                j++;
                tot++;
            }else
                i++;
        }
        if(j == s2.length())
            return tot;
        else
            return -1;
    }

    public String findLongestWord(String s, List<String> d) {
        String res = "";

        int maxMatchingLtrs = 0;

        for(String dictWord: d)
        {
            int ltrs  = compareStrings(s, dictWord);
           
            if(ltrs > maxMatchingLtrs)
            {
                maxMatchingLtrs = ltrs;
                res = dictWord;
            }else if(ltrs == maxMatchingLtrs)
            {
                if(dictWord.compareTo(res) < 0)
                    res = dictWord;
            }
        }
        return res;
        
    }

    public static void main(String[] args)
    {
        System.out.println(new LongestWordDict().findLongestWord("abpcplea", Arrays.asList(new String[]{"ale","apple","monkey","plea"})));
        //System.out.println(new LongestWordDict().findLongestWord("abpcplea", Arrays.asList(new String[]{"a","b","c"})));
        //System.out.println(new LongestWordDict().findLongestWord("aewfafwafjlwajflwajflwafj", Arrays.asList(new String[]{"apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"})));
    }
    
}
