import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        
        for(String[] arr: clothes) {
            map.put(arr[1], map.getOrDefault(arr[1],0)+1);
        }
        
        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            answer*=(entry.getValue()+1);
        }
        
        return answer-1;
    }
}