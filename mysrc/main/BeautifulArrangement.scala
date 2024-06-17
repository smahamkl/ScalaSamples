package mysrc.main

object BeautifulArrangement {
  def main(args: Array[String]): Unit = {
    println(countArrangement(4))
  }

  def printList(lst: Iterator[List[Int]]): Int = {
    var res = 0
    while (lst.hasNext) {
      val l = lst.next()
      for (item <- l) {
        print(item + ",")
      }
      println()
      res += 1
    }

    return res
  }
  def filterLists(l: List[Int]): Boolean = {
    //for 3
    var found = false
    for (i <- 1 until l.length by 2) {
      if (l(i - 1) == 3){
        found = true
      }
    }

    if (!found)
      return false

    for (i <- l.length to 1 by -1) {
      if (l(i - 1) % i != 0 && i % l(i - 1) != 0)
        return false
    }
    return true
  }
  def countArrangement(n: Int): Int = {
    val l = List.tabulate(n)(x => x + 1).permutations
    val l1 = l.filter {
      case s: List[Int] => filterLists(s)
      case _            => true
    }

    return printList(l1)
  }
}
