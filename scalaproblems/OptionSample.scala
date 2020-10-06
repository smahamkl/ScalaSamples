object OptionSample extends App {

  def toInt(value: String): Option[Int] = {

    try {
      Some(Integer.parseInt(value))
    } catch {
      case e: Exception => None
    }
  }

  toInt("3") match {
     case Some(i) => println(i)
     case None => println()
  }

  toInt("") match {
    case Some(i) => println(i)
    case None => println("No Value")
 }
}
