import scala.collection.mutable.HashMap
/*
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column 
and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
*/
object SortMatrixDiagonally{

    def rm(l: List[Int]):List[Int] = {
        l match {
            case x :: tail => tail
            case _ => Nil
        }
    }

    def diagonalSort(mat: Array[Array[Int]]): Array[Array[Int]] = {
        var nummap:HashMap[Int,List[Int]] = HashMap()

        for(row<-0 to mat.length-1)
        {
            for(col<-0 to mat(row).length-1)
            {
                val mapidx = row-col
                if(nummap.contains(mapidx)){
                    val l = mat(row)(col) :: nummap.get(mapidx).get
                    nummap += mapidx -> l
                }
                else
                    nummap += mapidx -> List(mat(row)(col))
            }
        }
        for((k,v)<-nummap)
            nummap += k -> v.sorted
        
        for(row<-0 to mat.length-1)
        {
            for(col<-0 to mat(row).length-1)
            {
                val mapidx = row-col
                if(nummap.contains(mapidx)){
                   mat(row)(col) = nummap.get(mapidx).get(0)
                   nummap += mapidx -> rm(nummap.get(mapidx).get)
                }
            }
        }
        mat
    }

    def main(args:Array[String]):Unit = {

        val l = diagonalSort(Array(Array(3,3,1,1),Array(2,2,1,2),Array(1,1,1,2)))
        for(row<-0 to l.length-1)
        {
            for(col<-0 to l(row).length-1)
                print(l(row)(col) + " ")
            println()
        }
    }
}