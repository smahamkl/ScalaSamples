package scalaproblems



object MonadSample extends App{
  val f = (i: Int) => List(i - 1, i, i + 1)
  val f1 = (i: Int) => List("pred=" + (i - 1), "succ=" + (i + 1))

  val f2 = (i: Int) => List(i + 1)
  val f3 = (i: Int) => List(i + 1)

  val list = List(5, 6, 7)
  println(list.flatMap(f1))

  //left-identity law -> unit(x).flatMap(f) == f(x)
  println(List.apply(3).flatMap(f2))
  println(f2(3))

  //right-identity law -> m.flatMap(unit) == m
  println(List(3).flatMap(y=>List.apply(y)))

  //associativity law -> m.flatMap(f).flatMap(g) == m.flatMap(x ⇒ f(x).flatMap(g))
  println(List.apply(3).flatMap(f2).flatMap(f3))
  println(List.apply(3).flatMap(x => f2(x).flatMap(f3)))

//  val getChild = (user: User) => user.child
//
//  def loadUser(name: String): Option[User] = {
//    /** get user * */
//    val u = new MyUser()
//    Some(u)
//  }
//
//  val result = loadUser("mike")
//    .flatMap(getChild)
//    .flatMap(getChild)

  println("Let's do some sequencing ...")

  // I want to get a user and see if he has a grandchild
  case class User(
                   child: Option[User],
                   name: String
                 )

  object UserService {
    def loadUser(name: String): Option[User] = Some(User(child = Some(User(child = Some(User(child = None, name = "Jan")), name = "Jef")), name = "Joe"))
  }


  // sequencing via flatmap
  val grandChild: Option[User] = UserService.loadUser("Kristof")
    .flatMap(u => u.child)
    .flatMap(u => u.child)

  println(grandChild.map(_.name).getOrElse("No grandchild found ..."))


  // sequencing via map
  val grandChildMap: Option[User] = UserService.loadUser("Kristof")
    .map(u => u.child)
    .map(u => u.get.child.get)

  println(grandChild.map(_.name).getOrElse("No grandchild found ..."))


}

