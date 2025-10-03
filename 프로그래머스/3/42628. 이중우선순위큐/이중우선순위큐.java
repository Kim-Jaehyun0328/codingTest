import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        PriorityQueue<Integer> maxQ = new PriorityQueue<>(Collections.reverseOrder());
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(String o : operations) {
            String[] s = o.split(" ");
            if(s[0].equals("I")) {
                minQ.offer(Integer.parseInt(s[1]));
                maxQ.offer(Integer.parseInt(s[1]));
                map.put(Integer.parseInt(s[1]), map.getOrDefault(Integer.parseInt(s[1]),0) + 1);
            }
            else if(o.equals("D 1")) {
               clean(maxQ, map);
                if(!maxQ.isEmpty()) {
                    int num = maxQ.poll();
                    map.put(num, map.get(num)-1);
                }
            } else if(o.equals("D -1")) {
                clean(minQ, map);
                if(!minQ.isEmpty()) {
                    int num = minQ.poll();
                    map.put(num, map.get(num)-1);
                }
            }
        }
        
        clean(maxQ, map);
        clean(minQ, map);
        
        if(maxQ.isEmpty() || minQ.isEmpty()) return answer;
        else {
            return new int[]{maxQ.peek(), minQ.peek()};
        }
        
    }
    
    // 큐 맨 앞이 죽은 값이면 버림
    private void clean(PriorityQueue<Integer> pq, HashMap<Integer,Integer> map) {
        while(!pq.isEmpty() && map.getOrDefault(pq.peek(),0) == 0) {
            pq.poll();
        }
    }
}