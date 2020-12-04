import java.util.ArrayList;

public class KthFactorOfN {
    ArrayList<Integer> factors = new ArrayList<Integer>();

    public void findFactors(int n) {
      for(int i=1;i<=n;i++){
         if(n % i == 0)
            factors.add(i);
      }
    }

    public int kthFactor(int n, int k) {
        findFactors(n);
        if(factors.size() >= k)
            return factors.get(k-1);
        else
            return -1;
    }

    public static void main(String[] args) {
        System.out.println(new KthFactorOfN().kthFactor(4,4));
    }
}
