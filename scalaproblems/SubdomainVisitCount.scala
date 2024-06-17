package scalaproblems

object SubdomainVisitCount extends App {

  def subDomains(cpdomain: String, cnt:Int): List[(String, Int)] = {
    if(cpdomain.indexOf(".") != -1)
      {
        (cpdomain, cnt)::subDomains(cpdomain.substring(cpdomain.indexOf(".")+1), cnt)
      }else{
      List((cpdomain, cnt))
    }
  }

  def subdomainVisits(cpdomains: Array[String]): List[String] = {

    val d = cpdomains.flatMap { x =>
      val t = x.split(" ");
      subDomains(t(1), t(0).toInt)
    }.groupBy(x1=> x1._1).map { case (key, value) => key -> (value.map(_._2)).sum}
    d.map(x => x._2 + " " + x._1).toList
  }

  private val subDomainArr = Array("9001 discuss.leetcode.com", "9001 discuss1.leetcode.com")
  println(subdomainVisits(subDomainArr))
}
