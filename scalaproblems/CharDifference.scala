package scalaproblems

object CharDifference extends App{

  def findTheDifference(s: String, t: String): Char = {
    var cmap = Map[Char, Int]()
    var res = '0'
    for(c <- t)
      cmap += c -> (cmap.getOrElse(c, 0) + 1)

    for(c <- s)
        cmap += c -> (cmap.getOrElse(c, 0) - 1)

    for(key <- cmap.keys) {
      if (cmap(key) > 0)
        res = key
    }

    res
  }

  val s = ""
  val t = "y"
  println(findTheDifference(s, t))
}
