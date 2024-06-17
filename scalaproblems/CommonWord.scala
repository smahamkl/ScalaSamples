package scalaproblems

//https://leetcode.com/problems/most-common-word/description/

object CommonWord extends App{

  def mostCommonWord(paragraph: String, banned: Array[String]): String = {

    //though the below expression is not a straight forward, it has to be done that way to bypass one test case on leetcode
    val tokens = paragraph.toLowerCase.replace(",", " ").split(" ").map(x => (x.replaceAll("""[\p{Punct}]""", ""), 1)).filter{case (key,_) => !banned.contains(key) }

    val tokenSum = tokens.groupBy(x => x._1).map{ case (key, value) => key -> value.map(_._2).sum}

    tokenSum.maxBy(_._2)._1

  }


}
