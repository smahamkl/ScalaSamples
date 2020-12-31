/*
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

*/
object LifeGame {
  def printArr(board: Array[Array[Int]]) = {
    for (row <- 0 to board.length - 1) {
      for (col <- 0 to board(row).length - 1) {
        print(board(row)(col) + " ")
      }
      println()
    }
  }

  def nextCell(row: Int, col: Int, board: Array[Array[Int]]): Int = {
    var totLiveCells: Int = 0
    //top diagonal left cell
    totLiveCells =
      if (row - 1 >= 0 && col - 1 >= 0 && board(row - 1)(col - 1) == 1)
        totLiveCells + 1
      else totLiveCells
    //top cell above
    totLiveCells =
      if (row - 1 >= 0 && board(row - 1)(col) == 1) totLiveCells + 1
      else totLiveCells
    //top diagonal right cell
    totLiveCells =
      if (
        row - 1 >= 0 && col + 1 < board(0).length && board(row - 1)(
          col + 1
        ) == 1
      )
        totLiveCells + 1
      else totLiveCells
    //same row left column
    totLiveCells =
      if (col - 1 >= 0 && board(row)(col - 1) == 1) totLiveCells + 1
      else totLiveCells
    //same row right column
    totLiveCells =
      if (col + 1 < board(0).length && board(row)(col + 1) == 1)
        totLiveCells + 1
      else totLiveCells
    //bottom diagonal left cell
    totLiveCells =
      if (
        row + 1 < board.length && col - 1 >= 0 && board(row + 1)(col - 1) == 1
      )
        totLiveCells + 1
      else totLiveCells
    //bottom diagonal right cell
    totLiveCells =
      if (
        row + 1 < board.length && col + 1 < board(0).length && board(row + 1)(
          col + 1
        ) == 1
      ) totLiveCells + 1
      else totLiveCells
    //bottom below cell
    totLiveCells =
      if (
        row + 1 < board.length && board(row + 1)(
          col
        ) == 1
      ) totLiveCells + 1
      else totLiveCells

    // println(
    //   row + "," + col + "," + ", array-val:" + board(row)(
    //     col
    //   ) + ", total live neighbors:" + totLiveCells
    // )
    val res = board(row)(col)
    if (board(row)(col) == 0 && totLiveCells == 3)
      return 1
    else if (board(row)(col) == 1 && totLiveCells < 2)
      return 0
    else if (board(row)(col) == 1 && totLiveCells > 3)
      return 0
    else
        return res
  }

  def gameOfLife(board: Array[Array[Int]]): Array[Array[Int]] = {

    if(board.length == 0)
        board
    val board_copy = Array.fill(board.length){Array.fill(board(0).length){0}}

    for (row <- 0 to board.length - 1) 
      for (col <- 0 to board(row).length - 1) 
        board_copy(row)(col) = board(row)(col)
      

    for (row <- 0 to board.length - 1) {
      for (col <- 0 to board(row).length - 1) {
        board(row)(col) = nextCell(row, col, board_copy)
      }
    }
    printArr(board)

    return board

  }

  def main(args: Array[String]): Unit = {
    val board: Array[Array[Int]] =
      Array(Array(0, 1, 0), Array(0, 0, 1), Array(1, 1, 1), Array(0, 0, 0))
    // val board: Array[Array[Int]] =
    //   Array(Array(1,1), Array(1,0))
    // val board: Array[Array[Int]] =
    //   Array(Array(1))
    gameOfLife(board)
  }
}
