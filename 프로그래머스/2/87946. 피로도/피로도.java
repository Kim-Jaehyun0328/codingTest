//dfs로 순서가 있는 배열을 만듦
//배열의 사이즈가 dungeons와 같으면 처리 시작

import java.util.*;

class Solution {
    static int ans = Integer.MIN_VALUE;
    static boolean[] visited;
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        DFS(k, dungeons, new ArrayList<int[]>());
        return ans;
    }
    
    private void DFS(int k, int[][] dungeons, List<int[]> dungeon) {
        if(dungeons.length==dungeon.size()) {
            int cnt = 0;
            for(int[] arr:dungeon) {
                //최소 필요 소모도가 k보다 작거나 같고, 소모 피로도가 k보다 작거나 같으면
                if(arr[0]<=k && arr[1]<=k) {
                    cnt++;
                    k -= arr[1];
                }
            }
            ans = Math.max(ans, cnt);
        } else {
            for(int i=0; i<dungeons.length; i++) {
                if(!visited[i]) {
                    visited[i] = true;
                    dungeon.add(dungeons[i]);
                    DFS(k, dungeons, dungeon);
                    visited[i] = false;
                    dungeon.remove(dungeons[i]);
                }
            }
        }
    }
}