import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        HashSet<String> set = new HashSet<>(Arrays.asList(phone_book));
        
        for(String num : phone_book) {
            StringBuilder sb = new StringBuilder();
            for(char c : num.toCharArray()) {
                sb.append(c);
                if(!num.equals(sb.toString()) && set.contains(sb.toString())) {
                    return false;
                }
            }
        }
        return true;
    }
}