import java.util.*;


public class AtoiImplementation {
    
    static int atoi(String str) {

        int val = 1;
        int lastIdx = 0;
        if(str.charAt(0) == '-')
        {
            val = -1;
            lastIdx = 1;
        }

        Map<String, Integer> numMap = new HashMap<>();

        // Your code here
        for(int i=0;i<=9;i++)
            numMap.put(""+i,  i);
        
        int power = 1;
        int res = 0;
                
        for(int i=str.length()-1;i>=lastIdx;i--)
        {
            String ch = String.valueOf(str.charAt(i));

            if(numMap.containsKey(ch))
                res += numMap.get(ch) * power;
            else
                return -1;
            
            power *= 10;

        }

        return res * val;
        
    }

    public static void main(String[] args)
    {
        System.out.println(atoi("-0"));
    }

}
