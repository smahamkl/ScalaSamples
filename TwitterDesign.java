import java.util.*;
/*
LeetCode 355
*/
public class TwitterDesign{

    private HashMap<Integer, LinkedList<TweetOrder>> userTweets;
    private HashMap<Integer, Set<Integer>> userFollowers;
    private int counter;

    public static final class TweetOrder{
        int counter;
        int tweetId;
        public TweetOrder(int _counter, int _tweetId)
        {
            this.counter = _counter;
            this.tweetId = _tweetId;
        }
    }

    public TwitterDesign() {
        userTweets = new HashMap<Integer, LinkedList<TweetOrder>>();
        userFollowers = new HashMap<Integer, Set<Integer>>();
        counter = 0;
    }
    
    public void postTweet(int userId, int tweetId) {
        //Maintain a hashmap of userid -> prioritylist(tweets)
        if(userTweets.containsKey(userId))
        {
            userTweets.get(userId).add(new TweetOrder(counter, tweetId));
        }else{
            LinkedList<TweetOrder> hm = new LinkedList<>();
            hm.add(new TweetOrder(counter, tweetId));
            userTweets.put(userId, hm);
        }
        counter++;
    }
    
    public List<Integer> getNewsFeed(int userId) {
        //get the user followers
        Set<Integer> userF;
        if(userFollowers.containsKey(userId))
         userF = userFollowers.get(userId);
        else
        userF = new HashSet<Integer>();
        userF.add(userId);

        TreeMap<Integer, Integer> tmpQ = new TreeMap<Integer, Integer>();

        for(Integer user: userF)
        {
            //get user tweets
            if(userTweets.containsKey(user))
            {
                LinkedList<TweetOrder> lto = userTweets.get(user);
                int index = lto.size()-1;
                int cnt = 0;
                while(index >=0 && cnt < 10)
                {
                    TweetOrder to = lto.get(index);
                    tmpQ.put(-to.counter, to.tweetId);
                    index--;
                    cnt++;
                }
                
            }
        }
        int cnt = 0;
        List<Integer> res = new ArrayList<>();
        for(Map.Entry<Integer,Integer> e: tmpQ.entrySet())
        {
            res.add(e.getValue());
            cnt++;
            if(cnt >= 10)
                break;
        }

        return res;
    }
    
    public void follow(int followerId, int followeeId) {
        Set<Integer> followerList;
        if(userFollowers.containsKey(followerId))
            followerList = userFollowers.get(followerId);
        else
            followerList = new HashSet<Integer>();
        followerList.add(followeeId);
        userFollowers.put(followerId, followerList);
    }
    
    public void unfollow(int followerId, int followeeId) {
        if(userFollowers.containsKey(followerId))
        {
            userFollowers.get(followerId).remove(followeeId);
        }
    }

    public static void printList(List<Integer> nf)
    {
        for(Integer news:nf)
        {
            System.out.print(news + "; ");
        }
        System.out.println();
    }

    public static void main(String[] args)
    {
        TwitterDesign td = new TwitterDesign();
        td.postTweet(1, 5);
        List<Integer> nf = td.getNewsFeed(1);
        printList(nf);
        td.follow(1, 2);
        td.postTweet(2, 6);
        nf = td.getNewsFeed(1);
        printList(nf);
        td.unfollow(1, 2);
        nf = td.getNewsFeed(1);
        printList(nf);

    }

}