object Practice1{
    def main(args: Array[String])
    {
        val testColl = List(1,2,3,4)
        val sum = testColl.foldLeft(0){(x,y) => {
            println(x);
            x+y
         }    
        }
        println(sum)
    }  
}