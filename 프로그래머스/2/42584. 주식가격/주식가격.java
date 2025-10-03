import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i<prices.length-1; i++) {
            int temp = 1;
            for(int j=i+1; j<prices.length-1; j++) {
                if(prices[i]<=prices[j]) temp++;
                else break;
            }
            arr.add(temp);
        }
        arr.add(0);
        answer = arr.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}