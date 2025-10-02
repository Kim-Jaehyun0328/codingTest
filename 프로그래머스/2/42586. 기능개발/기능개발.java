import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<>();
        Deque<Integer> dq = new ArrayDeque<>();
        
        for(int i=0; i<progresses.length; i++) {
            int day = 0;
            while(progresses[i]<100) {
                progresses[i] += speeds[i];
                day++;
            }
            dq.offer(day);
        }
        
        int temp = dq.poll();
        int cnt = 1;
        while(!dq.isEmpty()) {
            int num = dq.poll();
            if(num > temp) {
                temp = num;
                arr.add(cnt);
                cnt = 1;
            } else cnt++;
        }
        arr.add(cnt);
        
        answer = arr.stream().mapToInt(i->i).toArray();
        return answer;
    }
}