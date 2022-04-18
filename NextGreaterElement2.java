import java.util.Stack;

public class NextGreaterElement2 {

    public static long[] nextLargerElement(long[] arr, int n)
    { 
        // Your code here
        /*
        we need to maintain a monotonous stack that is continuous decreasing
        we compare the current ele with previous element and if its lower than previous
        push prev & cur to the stack
        if the cur element is greater than previous, update the next greater ele for previous
        Also pop the elemtns from stack until the current element is less than the element on stack
        repeat the steps
        */
        Stack<Integer> montIdx = new Stack<>();

        long[] res = new long[arr.length];
        res[arr.length-1] = -1;

        for(int i=1; i<arr.length;i++)
        {
            if(arr[i] > arr[i-1])
            {
                res[i-1] = arr[i];
                    while(!montIdx.isEmpty() && arr[i] > arr[montIdx.peek()])
                    {
                        int idx = montIdx.pop();
                        res[idx] = arr[i];
                    }
                
            }
            else{
                montIdx.push(i-1);
            }
        }

        while(!montIdx.isEmpty())
        {
            int idx  = montIdx.pop();
            res[idx] = -1;
        }

        return res;
    } 
    
    public static void main(String[] args)
    {
        NextGreaterElement2 obj = new NextGreaterElement2();
        //int[] res = obj.nextGreaterElement(new int[]{4,1,2} ,new int[]{1,3,4,2});
        long[] res = obj.nextLargerElement(new long[]{2,1} ,2);
        System.out.println(res.length);
        for(long ele : res){
            System.out.print(ele + ", ");
        }
    }

}
