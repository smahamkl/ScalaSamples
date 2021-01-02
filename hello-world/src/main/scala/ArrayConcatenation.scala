import scala.collection.mutable.HashMap
/*
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct.
Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false

 */
object ArrayConcatenation {

  def printMap(map: HashMap[Int, Int]) = {
    map.foreach { case (key, value) =>
      print(key + " -> " + value + "  ")
    }
    println()
  }

  def canFormArray(arr: Array[Int], pieces: Array[Array[Int]]): Boolean = {
    if (arr.length == 0 || pieces.length == 0)
      return false

    var arrMap: HashMap[Int, Int] = HashMap()
    arrMap += arr(0) -> -1
    for (i <- 1 to arr.length - 1) {
      arrMap += arr(i) -> arr(i - 1)
    }
    //printMap(arrMap)

    for (i <- 0 to pieces.length - 1) {
      if (pieces(i).length == 1 && arrMap.getOrElse(pieces(i)(0), -2) == -2) {
        return false
      } else {
        for (j <- 1 to pieces(i).length - 1) {
          //println(arrMap.getOrElse(pieces(i)(j), -2) + " " + pieces(i)(j - 1))
          if (arrMap.getOrElse(pieces(i)(j), -2) != pieces(i)(j - 1))
            return false
        }
      }
    }

    return true
  }

  def main(args: Array[String]) = {
    println(
      canFormArray(
        Array(85),
        Array(Array(85))
      )
    )
    // println(
    //   canFormArray(
    //     Array(1, 3, 5, 7),
    //     Array(Array(2), Array(4), Array(6), Array(8))
    //   )
    // )
    //println(canFormArray(Array(15,88), Array(Array(88), Array(15))))
    //println(canFormArray(Array(49,18,16), Array(Array(16,18,49))))
    // println(
    //   canFormArray(
    //     Array(91, 4, 64, 78),
    //     Array(Array(78), Array(4, 64), Array(91))
    //   )
    // )
  }
}
