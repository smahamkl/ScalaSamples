import scala.math
/*
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
*/
object LargestRectangle{

    def printArr(arr: Array[Int]) = {
        for(x<- arr)
            print(x + " ")
        
        println()
    }

    def largestRectangleArea(heights: Array[Int]): Int = {
        var arrl = heights.length
        var res = 0
        for(item<- heights)
        {
            res = math.max(res, item * arrl)
            arrl -= 1
        }

        return res
    }

    def main(args: Array[String]){
       println(largestRectangleArea(Array(2,1,5,2,6,5,7,2,3)))
    }
}