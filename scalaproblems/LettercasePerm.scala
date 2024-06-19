package scalaproblems

import scala.collection.mutable.Set

//https://leetcode.com/problems/letter-case-permutation/description/

object LettercasePerm extends App {

  def letterCasePermutation(s: String): List[String] = {

    def permutate(res:List[String], c:Char) = {
      if(c.isDigit)
        for(x <- res) yield x++c.toString
      else
        for(x <- res; y <- List(c.toUpper.toString, c.toLower.toString)) yield x++y
    }

    var res = List("")
    for(x<-0 until s.length) {
        res = permutate(res, s(x))
    }

    res
  }


//  def letterCasePermutation(s: String): List[String] = {
//    def permutate(per:String, s: String, idx: Int):Unit = {
//      if(per.length == s.length)
//        res += per
//      else {
//        if (s(idx).isDigit)
//          permutate(per + s(idx), s, idx + 1)
//        else {
//          permutate(per + s(idx).toLower, s, idx + 1)
//          permutate(per + s(idx).toUpper, s, idx + 1)
//        }
//      }
//    }
//    res.clear()
//    permutate("", s, 0)
//    res.toList
//  }

  val s = "abcd4"
  println(letterCasePermutation(s))
}
