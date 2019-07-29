object BinaryTreeSample2 {

  /*
             1
             |
        |        |
        2        3
      |  |     |   |
      4  5     6   7
   */

  def findLCA1(tree: Tree, x: Int, y: Int): Option[Tree] = {
    if (tree.value == x || tree.value == y) Some(tree)
    else (if (tree.left != None) findLCA1(tree.left.get, x, y) else None, if (tree.right != None) findLCA1(tree.right.get, x, y) else None) match {
      case (Some(r), Some(l)) => Some(tree)
      case (Some(r), None) => Some(r)
      case (None, Some(l)) => Some(l)
      case (None, None) => None
    }
  }

  def main(args: Array[String]) = {

    val tree = Tree(1,
      Some(Tree(2,
        Some(Tree(4, None, None)),
        Some(Tree(5, None, None))
      )),
      Some(Tree(3,
        Some(Tree(6, None, None)),
        Some(Tree(7, None, None))
      ))
    )

    //println(findLCA(tree, 5, 6))

    println(findLCA1(tree, 2, 4))

  }
}
case class Tree(value: Int, left: Option[Tree], right: Option[Tree])
