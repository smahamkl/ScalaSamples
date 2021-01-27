package jan2021challenge;

import java.util.Arrays;
/*
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
*/
class Solution {
    public boolean closeStrings(String word1, String word2) {
       int[] map = new int[26];
       int[] map2 = new int[26];
        for (char c : word1.toCharArray())
            map[c - 'a']++;
        
       for (char c : word2.toCharArray()) {
           if (map[c - 'a'] == 0)
               return false;
           
            map2[c - 'a']++;
       }
        
        
        Arrays.sort(map);
        Arrays.sort(map2);

        for(int i: map)
            System.out.print(i + " ");
        System.out.println();

        for(int i: map2)
            System.out.print(i + " ");
        System.out.println();
        
        return Arrays.equals(map, map2);
    }

    public static void main(String[] args)
    {
        System.out.println(new Solution().closeStrings("cabbba", "abbccc"));
    }
}