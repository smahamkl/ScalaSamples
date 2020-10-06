object QuickSort{
    def sort(xs: Array[Int])
    {
      def swap(i: Int, j: Int)
      {
          val t = xs(i); xs(i) = xs(j); xs(j) = t
      }
      def sort1(l: Int, r:Int)
      {
        val pivot = xs(r)
        var i = l;
        var j = l;
        while(j < r)
        {
            if(xs(j) <= pivot) {
                swap(i, j); 
            i+=1
            }

            j+=1
        }
        swap(i, r)
        if(l < (i-1)) sort1(l, i-1)
        if(r > (i+1)) sort1(i+1, r)
      }
      sort1(0, xs.length-1)
    }

    def sortFunc(xs: Array[Int]): Array[Int] = {
        if (xs.length <= 1) xs
        else {
            val pivot = xs(xs.length / 2)
            Array.concat(
            sortFunc(xs filter (pivot >)),
            xs filter (pivot ==),
            sortFunc(xs filter (pivot <)))
        }
    }
    def main(args: Array[String])
    {
      var xs = Array(50, 80, 70, 60, 23, 9, 18, 61,32)
      xs = sortFunc(xs)
      //xs.fold(0){(a,b) => {print(b + " "); a + b}}
      xs.foreach(println)
    }
}