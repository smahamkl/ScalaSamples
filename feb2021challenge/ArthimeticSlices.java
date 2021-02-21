package feb2021challenge;

/*
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two 
consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
*/
public class ArthimeticSlices {

    private int totalSlicesByLength(int n) {
        if (n < 3)
            return 0;
        int tot = n - 3 + 1;
        int ctr = 4;
        while (ctr <= n){
            tot += n - ctr + 1;
            ctr++;
        }
        return tot;
    }

    public int numberOfArithmeticSlices(int[] A) {
        int res = 0;

        if(A.length < 3)
            return res;

        int s = 0;
        int f = 1;
        int diff = A[f] - A[s];
        while (f < A.length - 1) {
            System.out.println("diff:" + diff + " f:" + f + " s:" + s);
            if (A[f+1] - A[f] != diff) {
                res += totalSlicesByLength(f - s + 1);
                s = f;
                diff = A[f+1] - A[f];
            }
            f++;
        }
        System.out.println("diff:" + diff + " f:" + f + " s:" + s);
        res += totalSlicesByLength(f - s + 1);
        return res;
    }

    public static void main(String[] args) {
        //System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] { 1, 2, 3, 4, 5 }));
        //System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] { 1,3,4,5, 6}));
        //System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] {1, 1, 2, 5, 8}));
       // System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] {1, 2,3,5,8,9,10}));
       //System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] {1, 3, 5, 7, 9}));
       System.out.println(new ArthimeticSlices().numberOfArithmeticSlices(new int[] {}));
    }

}
