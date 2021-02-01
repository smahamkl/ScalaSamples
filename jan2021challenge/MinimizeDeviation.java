/*
Minimize deviation in an array

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Solution:
--------------
Key takeaways

We can half a number multiple times until it odd but we can only dobule a number at most once because we can only double it when it is odd.
Approach
It is easy for us to make all numbers their maximum possible value. This has two consequences.

The lowest number is a multiple of 2 and so there is no even number that is lower.
It is not possible to make any number larger than the ones we have.
We can iterate through all numbers, doubling any that are add and adding them to a priority queue. Whilst doing this we track the smallest number.
We use a custom comparator to ensure that the priority queue has largest number with highest priority and so they come out first.
We then repeatedly remove elements from queue, half them, update the min number and the delta and put the number back. This ensure that we always reduce the size of the largest element and if it becomes less than the current smallest number we update the new minimum. We then remove the new largest number from the queue and calculate an updated delta if the new delta is smaller than the old one.
We note that we now always the smallest number as close as possible to the largest number. This means that once we find an odd number as the largest number we can reduce the delta any more.

The overall Time Complexity is O(Nlog(M)log(N)) where M is the average size of the largest number, because we iterate over the whole at least twice O(N), inserting and removing items from a priority queue, each operation of which is O(logN) time complexity. In addition we may iterate over a number multiple times if it is a power of 2 so in the worst case we iterate over all number O(log(M)) times, where M is the size of the number.
Space Complexity is O(N) because we have a priority queue to store all the items of the input array.

Optimizations & Simplifications
To make the priority queue yield the largest rather than the smallest number I used a custom comparator to reverse the default comparison. I felt this was easier to understand than making number negative.
I also observed that if the same number has already been seen we don;t need to process it again. Repeating numbers will appear as adjacent values in the priority queue, so I remember the previous number removed from the queue and if it matches the current number I don't process the number and add it back to the queue.

If you find this helpful, please upvote! It will greatly encourage me to write more like this in the future. Thank you! 

*/
import java.util.Queue;
import java.util.PriorityQueue;

class MinimizeDeviation {
    public int minimumDeviation(int[] nums) {
        // Use custom comparator to reverse priority order so largest number has highest priority
		// Space O(N)
        Queue<Integer> pq = new PriorityQueue<>((Integer o1, Integer o2)->o2-o1);
		// Need to keep track of minimum value
        int first = Integer.MAX_VALUE;
        // Set array to maximum values
        // Will make all numbers even if not already even
        // O(Nlog(N)) Time
        for (int num : nums) {
		    // If number is odd we can double it
            if ((num % 2) == 1)
                num *= 2;
			// Add number to queue and update smalled number in queue
            // O(log(N)) Time
            pq.add(num);
            first = Math.min(first, num);
        }

        // Iterate until there is an odd number as largest
        // O(Nlog(N))
        int last = pq.remove();
        int prev = last+1;
        int delta = last - first;
        while ((last%2) == 0) {
            // If number previously seen then don't add it back in
            // This removes duplicate numbers and so reduces time
            if (last != prev) {
				// Half last number removed and add it back to queue
                // O(log(N))
                prev = last;
                last /= 2;
                pq.add(last);
                first = Math.min(last, first);
            }
			// FInd new largest and update delta if lower
            last = pq.remove();
            delta = Math.min(delta, last - first);
        }
        return delta;
    }

    public static void main(String[] args)
    {
        System.out.println(new MinimizeDeviation().minimumDeviation(new int[]{4,1,5,20,3}));
    }
}
