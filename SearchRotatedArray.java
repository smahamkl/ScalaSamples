public class SearchRotatedArray {
    int search(int A[], int l, int h, int key)
    {
        // Complete this function
        int m = (l + h) / 2;
        if(key == A[m])
            return m;
        else if(l == h && A[l] == key)
            return l;
        else if(l == h && A[l] != key)
          return -1;

        if(A[l] < A[m])
        {
            if(key >= A[l] && key < A[m])
                return search(A, l, m-1, key);
            
            return search(A, m+1, h, key);
        }

        if(key > A[m] && key <= A[h])
            return search(A, m+1, h, key);
        
        return search(A, l, m-1, key);
    }

    public static void main(String[] args)
    {
        SearchRotatedArray obj = new SearchRotatedArray();
        System.out.println(obj.search(new int[]{5, 6, 7, 8, 9, 10, 1, 2, 3}, 0, 8, 10));
        System.out.println(obj.search(new int[]{3,5,1,2}, 0, 3, 4));
       
    }
}
