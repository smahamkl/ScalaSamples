object Sample1 extends App{
val a = List(1,2,3,4,5)

val a1 = a map {x=> x + 2}

//a1.foreach(println)

var myList: List[List[Int]] = List()

for(a <- Array.range(1,5);b <- Array.range(6,10))
   myList =  myList ::: List(List(a, b))


myList.flatten.foreach(println)

}