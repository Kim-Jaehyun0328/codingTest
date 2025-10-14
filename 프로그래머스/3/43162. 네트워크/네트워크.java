/*
1. BFS 활용, checked 배열 사용하기
2. q에 0부터 넣고 시작 (checked[0]=true 기본값)
3. 자기 자신+이미 추가된 것 제외하고 큐에 추가
4. 큐가 비워지면 하나의 네트워크임으로 +1
5. checked에 true인 부분부터 반복
*/

import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int ans = 0;
        Queue<Integer> q = new LinkedList<>();
        boolean[] checked = new boolean[n];
        boolean flag = true;
        while(flag) {
            flag = false;
            for(int i=0; i<n; i++) {
                if(!checked[i]) {
                    flag = true;
                    q.add(i);
                    checked[i] = true;
                    ans++;
                    break;
                }
            }
            while(!q.isEmpty()) {
                int num = q.poll();
                for(int i=0; i<n; i++) {
                    if(computers[num][i]==1 && !checked[i]) {
                        q.offer(i);
                        checked[i] = true;
                    }
                }
            }
            
        }
        return ans;
    }
}