import scala.collection.mutable.HashMap

/*
LeetCode - 560
Subarray Sum Equals K
https://www.youtube.com/watch?v=fFVZt-6sgyo
*/

object Solution extends App{

        def subarraySum(nums: Array[Int], k: Int): Int = {

        var prefixMap = new HashMap[Int, Int]().withDefaultValue(0)

        var psum = 0
        var res = 0
        prefixMap += 0 -> 1
        for(i <- 0 until nums.length)
        {
            psum += nums(i)

            if(prefixMap.contains(psum - k))
            {
                res += prefixMap.get(psum - k).get
            }
            prefixMap.put(psum, prefixMap.getOrElse(psum, 0) + 1)
        }

        return res
        
    }

    println(subarraySum(Array(1,2,3), 3))
    println(subarraySum(Array(), 0))
}