object ForComprehnsnSample extends App {
  case class Book(title: String, authors: List[String])

  val books: List[Book] =
    List(
      Book(
        "Structure and Interpretation of Computer Programs",
        List("Abelson, Harold", "Sussman, Gerald J.")
      ),
      Book(
        "Principles of Compiler Design",
        List("Aho, Alfred", "Ullman, Jeffrey")
      ),
      Book("Programming in Modula-2", List("Wirth, Niklaus")),
      Book("Introduction to Functional Programming", List("Bird, Richard")),
      Book(
        "The Java Language Specification",
        List("Gosling, James", "Joy, Bill", "Steele, Guy", "Bracha, Gilad")
      )
    )

  var finalList: List[Book] = List()

  finalList = for { book <- books if (isLastName(book.authors, "Ullman")) } yield
    book

  println(finalList.size)
  finalList.foreach(x => println(x.title + " " + x.authors))

  def isLastName(authors: List[String], name: String): Boolean = {

    authors.exists(author => author.split(",").head.trim() == name)
  }
}
