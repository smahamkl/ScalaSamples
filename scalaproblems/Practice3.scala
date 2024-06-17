object Practice3{

    def findLCA(node:MyNode, val1: Int, val2: Int): Option[MyNode] = {
        if(node.value == val1 || node.value == val2) Some(node)
        else(
            if(node.left != None) findLCA(node.left.get, val1, val2)  else None,
            if(node.right != None) findLCA(node.right.get, val1, val2) else None
        ) match {
            case (Some(l), Some(r)) => Some(node)
            case (Some(l), None) => Some(l)
            case (None, Some(r)) => Some(r)
            case (None, None) => None
        }
    }

    def main(args: Array[String]): Unit = {
            val tree = MyNode(1,
      Some(MyNode(2,
        Some(MyNode(4, None, None)),
        Some(MyNode(5, None, None))
      )),
      Some(MyNode(3,
        Some(MyNode(6, None, None)),
        Some(MyNode(7, None, None))
      ))
            )
      println(findLCA(tree, 5, 6).get)
    } 

    case class MyNode(value: Int, left: Option[MyNode], right:Option[MyNode])
}