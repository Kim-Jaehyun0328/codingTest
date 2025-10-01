import java.util.*;
class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int answer = nums.length/2;
        
        for(int num:nums) {
            map.put(num, map.getOrDefault(num,0) + 1);
        }
        if(map.size() >= answer) return answer;
        else return map.size();
        
    }
}