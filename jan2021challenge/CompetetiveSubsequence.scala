/*
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position 
where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more 
competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is 
the most competitive.
*/
object CompetetiveSubsequence{
    def mostCompetitive(nums: Array[Int], k: Int): Array[Int] = {
        var left =  0
        var res:Array[Int]  = Array()
        for(n<-k to 1 by -1){
            for(a<-left to nums.length-n){
                if(nums(a) < nums(left))
                    left = a
            }
            res = res :+ nums(left)
            left += 1
        }
        return res
    }

    def main(args:Array[String]):Unit = {
        //val inArr:Array[Int] = Array(2,4,3,3,5,4,9,6)
        val inArr:Array[Int] = Array(3,2)
        val res:Array[Int] = mostCompetitive(inArr, 2)
        for(a<-0 to res.length-1)
            print(res(a) + ",")
    }
}