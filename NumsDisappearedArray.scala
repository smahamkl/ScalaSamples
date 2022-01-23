import scala.math._
import scala.util.Sorting
import scala.collection.mutable.HashMap

/*
LeetCode - 448

Find All Numbers Disappeared in an Array
*/

object Solution extends App{
    def findDisappearedNumbers(nums: Array[Int]): List[Int] = {

        var minv = Int.MaxValue
        var maxv = Int.MinValue
        var total = 0
        val numMap = new HashMap[Int, Int]().withDefaultValue(0)

        nums.foreach(x =>  {
            minv = math.min(minv, x)
            maxv = math.max(maxv, x)
            total+=1
            numMap(x) += 1
        }
        )

        // numMap foreach {
        //     case (k, v) => println(k, v)
        // }
        // println(minv, maxv, total, numMap)
        for(x <- minv to maxv)
        {
            if(numMap.contains(x)){
                numMap.remove(x)
            }
            else {
                numMap(x) += 1
                }
        }

        return List.range(1, minv) ++ numMap.keySet.toList ++ List.range(maxv+1, total+1)
    }

   val x = findDisappearedNumbers(Array(3,3,3))
   println(x)

   val x1 = findDisappearedNumbers(Array(1,1))
   println(x1)
   
}