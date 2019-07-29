/*
METHOD 2 (Use Queue)
Algorithm:
For each node, first the node is visited and then it’s child nodes are put in a FIFO queue.
printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children (first left then right children) to q
    c) Dequeue a node from q and assign it’s value to temp_node
Time Complexity: O(n) where n is number of nodes in the binary tree
 */
object BreadthFirstSample2 extends App {

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

  var nodeList: mutable.ListBuffer[Node] = mutable.ListBuffer[Node]()
  breadthFirstSearch(root)


  def breadthFirstSearch(r: Node) = {

    nodeList += root

    while (nodeList.size > 0) {

      val tmp:Node = nodeList.remove(0)
      println(tmp.data)

      if (tmp.left != null)
        nodeList += tmp.left

      if (tmp.right != null)
        nodeList += tmp.right
    }
  }

}
