import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        int tot = 0;
        for(int i=0; i<truck_weights.length; i++) {
            while(true) {
                if(q.isEmpty()) {
                    tot+=truck_weights[i];
                    q.offer(truck_weights[i]);
                    answer++;
                    break;
                } else if(q.size()==bridge_length) {
                    tot-=q.poll();
                } else {
                    if(tot+truck_weights[i]<=weight) {
                        tot+=truck_weights[i];
                        q.offer(truck_weights[i]);
                        answer++;
                        break;
                    } else {
                        q.offer(0);
                        answer++;
                    }
                }
            }
        }
        
        answer+=(bridge_length);
        
        return answer;
    }
}