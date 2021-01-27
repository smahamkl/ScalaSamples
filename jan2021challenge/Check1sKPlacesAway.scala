import scala.collection.mutable.ListBuffer
object Check1sKPlacesAway{

    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var counter = k
        for(i<-0 to nums.length-1){
            if(nums(i) == 1){
                if(counter < k)
                    return false
                counter = 0
            }
            else
                counter+=1
        }
        return true
    }

    def main(args:Array[String]):Unit = {
        println(kLengthApart(Array(1,0,0,1,0,1), 2))
        println(kLengthApart(Array(0,1,0,1), 1))
        println(kLengthApart(Array(1,1,1,1,1), 0))
        println(kLengthApart(Array(1,0,0,0,1,0,0,1), 2))
        def sum = (x:Int, y:Int) => x+y
        var l = List(1,2,3,6,5)
        l = l.sortWith(_ > _)
        l = l :+ 7
        var m = List(6,7,8)
        var n = l:::m
        val n1 = n.map(x => x * 2)
        println(n1)
        println(n1.head + "   :" + n1.tail)
        println(n1.lastOption.get)
        println(sum(2,3))
        val o = for(i<-n1) yield i
        println(o)
    }
}