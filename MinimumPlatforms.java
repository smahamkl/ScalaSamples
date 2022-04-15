import java.util.*;

import javax.lang.model.util.ElementScanner6;

public class MinimumPlatforms {
    public final static class TrainTiming implements Comparable<TrainTiming>{

        public int time;
        public int type;

        public TrainTiming(int time, int type)
        {
            this.time = time;
            this.type = type;
        }
        @Override
        public int compareTo(TrainTiming that)
        {
             if(this.time == that.time)
                return this.type - that.type;
            else
                return this.time - that.time;

        }
    }
    static int findPlatform(int arr[], int dep[], int n)
    {
        // add your code here
        List<TrainTiming> tlst = new ArrayList<TrainTiming>();

        for(int i=0;i<n;i++)
        {
            tlst.add(new TrainTiming(arr[i], 0));

            tlst.add(new TrainTiming(dep[i], 1));
        }
        Collections.sort(tlst);

        int totalPlatforms = 0;
        int tmp = 0;
        for(int i = 0; i< tlst.size();i++)
        {
            TrainTiming t = tlst.get(i);

            //System.out.println(k.type + "," + k.time);
            if(t.type == 0)
                tmp += 1;
            else
                tmp -= 1;

            totalPlatforms = Math.max(totalPlatforms, tmp);
        }

        return totalPlatforms;
        
    }

    public static void main(String[] args)
    {
        MinimumPlatforms obj = new MinimumPlatforms();

        System.out.println(obj.findPlatform(new int[]{900, 940, 950, 1100, 1500, 1900}, new int[]{910, 1200, 1120, 1130, 1900, 2000}, 6));

        System.out.println(obj.findPlatform(new int[]{900,1100, 1235}, new int[]{1000,1200,1240}, 3));
    }
    
}
