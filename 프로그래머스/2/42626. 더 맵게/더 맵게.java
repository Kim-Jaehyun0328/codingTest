import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int s:scoville) pq.offer(s);
        
        while(!pq.isEmpty()) {
            if(pq.peek()>=K) return answer;
            int n1 = pq.poll();
            int n2 = 0;
            if(pq.size()>0) n2 = pq.poll();
            else return -1;
            int n3 = n1 + (n2*2);
            pq.offer(n3);
            answer++;
        }
        
        
        return -1;
    }
}