import java.util.*;

class Info {
    //번호, 요청시간, 소요시간
    int req, time;
    Info(int b, int c) {
        req=b; time=c;
    }
}

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, (a,b) -> a[0]-b[0]);
        PriorityQueue<Info> pq = new PriorityQueue<>((a,b) -> a.time-b.time);
        
        
        int now = 0;
        int idx = 0;
        int n = jobs.length;
        int cnt = 0;
        
        while(cnt<n) {
            while(idx<n && jobs[idx][0] <= now) {
                pq.offer(new Info(jobs[idx][0], jobs[idx][1]));
                idx++;
            }
            if(pq.isEmpty()) {
                now = jobs[idx][0];
            } else {
                Info i = pq.poll();
                now += i.time;
                answer += (now-i.req);
                cnt++;
            }
        }
        
        answer /= jobs.length;
        
        return answer;
    }
}