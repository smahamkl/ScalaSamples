/*
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Solution:
--------------
The first thing we should be able to understand is that one of the operations increases X while the other one decreases it. So the natural tendency is to think about the solution in terms of applying these operations in order. That is, multiply as many times as you need to before subtracting as many times as you need to.

We see that that's not a viable solution, however, once we recognize that one of the operations is quite obviously multiplicative rather than additive, meaning that a subtraction done before a multiplication has twice the impact, for example.

So the trick here is to think of the problem backwards: moving from Y to X instead of from X to Y. If Y is odd, we're forced to do the additive operation (reversed from the subtractive operation) as we can't divide an odd number by 2 and be able to reach X. If Y is even, we can prioritize the division operation instead. At each step we can increment our ans.

Once Y drops below X, the remaining difference must be made via the additive operation, so we can just return that difference plus ans.
*/
class BrokenCalculator {

    public int brokenCalc(int X, int Y) {
        int ans = 0;
        while (X < Y) {
            ans++;
            if (Y % 2 > 0) Y++;
            else Y /= 2;
        }
        return X - Y + ans;
    }

    public static void main(String[] args) {
        // System.out.println(new BrokenCalculator().brokenCalc(2, 3));
        // System.out.println(new BrokenCalculator().brokenCalc(5, 8));
        System.out.println(new BrokenCalculator().brokenCalc(3, 10));
    }
}