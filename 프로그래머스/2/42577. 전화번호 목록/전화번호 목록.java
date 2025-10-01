import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>();
        //O(n)
        for(String num:phone_book) {
            set.add(num);
        }
        
        for(String num:phone_book) {
            String temp = "";
            for(char c : num.toCharArray()) {
                temp += c;
                if(!num.equals(temp) && set.contains(temp)) return false;
            }
        }
        
        
        return true;
    }
}
