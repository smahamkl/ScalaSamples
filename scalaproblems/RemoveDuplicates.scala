object  RemoveDuplicates {

  def removeDups(xs: List[String]): List[String] = {
    if(xs.isEmpty) xs
    else{
      xs.head :: removeDups(xs.tail filter (x => x != xs.head))
    }
  }
  def main(args: Array[String]) = {
    val xs = List("A", "A", "B", "B", "C", "C")
    println("Size of original array: " + xs.size)
    val xs1 = removeDups(xs)
    println("size after removing all dups: " + xs1.size)
    xs1.foreach(println)
  }
}
