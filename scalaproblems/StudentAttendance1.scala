package scalaproblems

//https://leetcode.com/problems/student-attendance-record-i/

object StudentAttendance1 extends App{

  def checkRecord(s: String): Boolean = {
    val late = s.foldLeft(0){(a,c) => if(a == 3) 3 else{if(c == 'L') a+1 else 0}}

    val abs = s.foldLeft(0){(a,c) => if(c == 'A') a + 1 else a + 0}

    if(late == 3 || abs >= 2)
      false
    else
      true
  }

}
