object LastElementList extends App {
  val a = List(1, 2, 3, 4, 5)

  println(lastElement(a))

  val a1 = List("A", "B", "C", "D", "E")

  println(lastElement(a1))

  def lastElement[A](list: List[A]): A = list match {
    case Nil       => null.asInstanceOf[A]
    case xs :: Nil => xs
    case xs :: ls  => lastElement(ls)
  }
}
