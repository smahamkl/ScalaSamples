object DepthFirstSamples1 extends App {

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
  postOrderTraversal(root)
  println("-------------------------")
  InOrderTraversal(root)
  println("-------------------------")
  PreOrderTraversal(root)

  def postOrderTraversal(r: Node): Unit = {
    if (r != null) {
      postOrderTraversal(r.left)
      postOrderTraversal(r.right)
      println(r.data)
    }
  }

  def InOrderTraversal(r: Node): Unit = {
    if (r != null) {
      InOrderTraversal(r.left)
      println(r.data)
      InOrderTraversal(r.right)
    }
  }

  def PreOrderTraversal(r: Node): Unit = {
    if (r != null) {

      println(r.data)

      PreOrderTraversal(r.left)

      PreOrderTraversal(r.right)
    }
  }
}
