package jan2021challenge;
/*
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
*/
class KthMissingNumber {

    public int findKthPositive(int[] arr, int k) {
        int missing = 1, idx = 0, counter = 1;

        while (true) {
            if (idx < arr.length && counter == arr[idx]) {
                idx++;
            } else {
                missing = counter;
                k--;
            }

            if (k == 0)
                return missing;
            counter++;
        }
    }

    public static void main(String[] args) {
        System.out.println(new KthMissingNumber().findKthPositive(new int[] { 2, 3, 4, 7, 11 }, 5));
        System.out.println(new KthMissingNumber().findKthPositive(new int[] { 1, 2, 3, 4 }, 2));
        System.out.println(new KthMissingNumber().findKthPositive(new int[] {}, 5));
        System.out.println(new KthMissingNumber().findKthPositive(new int[] { 2 }, 1));
    }
}