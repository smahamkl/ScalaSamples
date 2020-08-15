object NQueenSample {

  val N: Int = 6;

  def placeQueens(k: Int): List[List[(Int, Int)]] = {
    if (k == 0)
      List(Nil)
    else {
      for {
        queens <- placeQueens(k - 1)
        col <- 1 to N
        queen = (k, col)
        if (isSafe(queen, queens))
      } yield queen :: queens

    }
  }

  def main(args: Array[String]) = {
    val solutions = placeQueens(N)
    println(solutions.size + " solutions found")
    // print the board of the first solution
    for (queen <- solutions.head; x <- 1 to N) {
      if (queen._2 == x) print("Q ") else print(". ")
      if (x == N) println()
    }

    println("------------------------------------------")
    for (queen <- solutions.tail.head; x <- 1 to N) {
      if (queen._2 == x) print("Q ") else print(". ")
      if (x == N) println()
    }
  }

  def isSafe(queen: (Int, Int), queens: List[(Int, Int)]): Boolean = {

    queens forall (!isAttacked(queen, _))
  }

  def isAttacked(queen1: (Int, Int), queen2: (Int, Int)): Boolean = {

    queen1._1 == queen2._1 || queen1._2 == queen2._2 ||
    Math.abs(queen1._1 - queen2._1) == Math.abs(queen1._2 - queen2._2)
  }
}
