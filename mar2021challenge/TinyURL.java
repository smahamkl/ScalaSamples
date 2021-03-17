package mar2021challenge;

import java.util.*;
/*
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
*/

class TinyURL {
    Map<String, String> codeDB = new HashMap<>(), urlDB = new HashMap<>();
    static final String chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    private String getCode() {
        char[] code = new char[6];
        for (int i = 0; i < 6; i++)
            code[i] = chars.charAt((int) (Math.random() * 62));
        return "http://tinyurl.com/" + String.valueOf(code);
    }

    public String encode(String longUrl) {
        if (urlDB.containsKey(longUrl))
            return urlDB.get(longUrl);
        String code = getCode();
        while (codeDB.containsKey(code))
            code = getCode();
        codeDB.put(code, longUrl);
        urlDB.put(longUrl, code);
        return code;
    }

    public String decode(String shortUrl) {
        return codeDB.get(shortUrl);
    }

    public static void main(String[] args) {
        TinyURL sol = new TinyURL();
        String encdStr = sol.encode("http://leetcode.com/sample1");
        System.out.println(encdStr);
        System.out.println(sol.decode(encdStr));
        encdStr = sol.encode("http://leetcode.com/sample2");
        System.out.println(encdStr);
        System.out.println(sol.decode(encdStr));
    }
}