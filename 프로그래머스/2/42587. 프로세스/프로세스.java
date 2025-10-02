import java.util.*;
class Position {
    int pr;
    int idx;
    Position(int a, int b) {
        pr=a; idx=b;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        Queue<Position> q = new LinkedList<>();
        for(int i=0; i<priorities.length; i++) {
            q.offer(new Position(priorities[i], i));
        }
        
        int max = Integer.MIN_VALUE;
        boolean flag = false;
        while(true) {
            //최대값 구해두기
            if(!flag) {
                for(Position n:q) {
                    max = Math.max(max, n.pr);
                }
                flag = true;
            }
            Position p = q.poll();
            if(p.idx==location && max==p.pr) break;
            if(max==p.pr) {
                answer++;
                flag = false;
                max=Integer.MIN_VALUE;
            } else {
                q.offer(p);
            }
        }
        
        
        return answer;
    }
}