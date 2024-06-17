package scalaproblems

import java.time.LocalDate

class AuxConstructor(val id:Int, val name:String) {

  private var localAppDate: LocalDate = LocalDate.now()

  def this (id:Int, name:String, _localdate: LocalDate) = {
    this(id, name)
    localAppDate = _localdate
  }

}

object AuxConstructor extends App{
  val myo = new AuxConstructor(1, "siva", LocalDate.now().minusDays(2))
  println(myo.localAppDate)
}