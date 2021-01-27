
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
    }
}