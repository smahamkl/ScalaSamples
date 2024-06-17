package mysrc.main

import scala.math
import scala.collection.mutable.Stack
/*
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Solution:
---------
The key is to use a increasing stack
Increasing stack can keep track of the first smaller on left and right for each element. By using this property, 
the maximal rectangle in histogram can be solved by using a stack in O(n).

 */
object LargestRectangle {

  def printArr(arr: Array[Int]) = {
    for (x <- arr)
      print(x + " ")

    println()
  }

  def largestRectangleArea(heights: Array[Int]): Int = {
    var ans = 0
    var harr = Array.fill(heights.length+2){0}
    for(i<-1 to heights.length)
        harr(i) = heights(i-1)
    harr(0)  = -1
    harr(heights.length+1) = -1
    var n = harr.length
    var stck = Stack[Int](0)
    for(i<-0 to n-1)
    {
        while(harr(i) < harr(stck.top))
        {
            var h = harr(stck.pop())
            var area = h * (i - stck.top -1)
            ans = math.max(ans, area)
            //println(harr(i) + " " + h + " " + area + " " + ans)
        }
        stck.push(i)
    }
    return ans
  }

  def main(args: Array[String]) {
    println(largestRectangleArea(Array(5,5,5,5,5,2,1,5,6,5,2,3)))
  }
}
