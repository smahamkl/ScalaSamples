//Breadth first search implementation, time complexity if n * n
//Time Complexity: O(n^2) in worst case. For a skewed tree, printGivenLevel() takes O(n) time where n is the number of nodes in the skewed tree.
// So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).

object BinaryTreeSample extends App {

  val root = new Node
  root.data = "1"
  root.right = new Node
  root.right.data = "3"
  root.left = new Node
  root.left.data = "2"
  root.left.left = new Node
  root.left.left.data = "4"
  root.left.right = new Node
  root.left.right.data = "5"
  root.left.right.right = new Node
  root.left.right.right.data = "6"
  root.left.right.right.right = new Node
  root.left.right.right.right.data = "7"

  var height: Int = findHeight(root)

  for (i <- 1 to height)
    printLevelTraversal(root, i)


  //every time it goes down (level) times towards left & right
  //and then print the data at that level
  def printLevelTraversal(r: Node, level: Int): Unit = {
    if (r != null) {
      if (level == 1)
        println(r.data)
      else if (level > 1) {
        printLevelTraversal(r.left, level - 1)
        printLevelTraversal(r.right, level - 1)
      }
    }
  }

  //typical divide and sub problem concept
  def findHeight(r: Node): Int = {
    if (r == null)
      return 0
    else {
      val lHeight: Int = findHeight(r.left)
      val rHeight: Int = findHeight(r.right)
      return Math.max(lHeight, rHeight) + 1
    }
  }
}
