package mysrc.main


class Task(val description: String) {
  private var _status: String = "pending"

  def status():String = _status
}

object Task {
  def apply(description: String): Task = new Task(description)

  def apply(description: String, status: String): Task = {
    val task = new Task(description)
    task._status = status
    task
  }

  def main(args: Array[String]) {

    // Creating object of AreaOfRectangle class
    var obj = Task("hello world")
    print(obj._status)
  }
}
