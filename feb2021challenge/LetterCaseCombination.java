package feb2021challenge;

import java.util.List;
import java.util.ArrayList;
/*
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
*/
public class LetterCaseCombination {
    public void buildPermutations(List<String> res, String per, String S, int i) {
        if (i < S.length()) {
            String curCh = String.valueOf(S.charAt(i));
            if (curCh.toLowerCase() != curCh.toUpperCase()) {
                buildPermutations(res, per + curCh.toLowerCase(), S, i + 1);
                buildPermutations(res, per + curCh.toUpperCase(), S, i + 1);
            }else
                buildPermutations(res, per + curCh, S, i + 1);
        } else 
            res.add(per);
    }

    public List<String> letterCasePermutation(String S) {
        List<String> res = new ArrayList<String>();
        buildPermutations(res, "", S, 0);
        return res;
    }

    public static void main(String[] args) {
        LetterCaseCombination sol = new LetterCaseCombination();
        //List<String> res = sol.letterCasePermutation("a1b2");
        List<String> res = sol.letterCasePermutation("");
        for (String s : res) {
            System.out.println(s);
        }
    }
}
