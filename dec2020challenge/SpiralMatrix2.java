package dec2020challenge;
/*
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
*/
public class SpiralMatrix2 {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int i = 1, row = 0, col = 0;
        char dir = 'R';

        while (i <= n * n) {
            switch (dir) {
                case 'R':
                    res[row][col] = i;
                    col++;
                    if (col == n || res[row][col] > 0){
                        dir = 'D';
                        col--;
                        row++;
                    }
                    break;
                case 'D':
                    System.out.println("Down:" + row + " " + col  + " " + i);
                    res[row][col] = i;
                    row++;
                    if (row == n || res[row][col] > 0){
                        dir = 'L';
                        col--;
                        row--;
                    }
                    break;
                case 'L':
                    System.out.println("Left:" + row + " " + col  + " " + i);
                    res[row][col] = i;
                    col--;
                    if (col+1 == 0 || res[row][col] > 0){
                        dir = 'U';
                        row--;
                        col++;
                    }
                    break;
                case 'U':
                System.out.println("Up:" + row + " " + col  + " " + i);
                    res[row][col] = i;
                    row--;
                    if (res[row][col] > 0){
                        dir = 'R';
                        row++;
                        col++;
                    }
                    break;
            }
            i++;
        }
        return res;
    }

    public static void printArr(int[][] arr) {
        for (int[] sarr : arr) {
            for (int item : sarr) {
                System.out.print(item + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] res = new SpiralMatrix2().generateMatrix(1);
        printArr(res);

    }
}
