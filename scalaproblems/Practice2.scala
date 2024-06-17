object Practice2{

    def toInt(value: String): Option[Int] = {
        try {
            Some(Integer.parseInt(value))
        }catch{
            case ex:NumberFormatException => Some(0)
        }
    }
    def main(args: Array[String])
    {
        val l = List("12", "23", "34", "45", "5","6", "", "None")

        val i = toInt("sdfasdasdasd") match {
            case Some(i1) => i1
            case None => 0
        }

        println(i)
        println("---------------------------")

        val k = l.flatMap(toInt(_)).sum

        println(k)
        //k.foreach(println)
    } 
}