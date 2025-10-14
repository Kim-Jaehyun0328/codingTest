/*
1. BFS 사용
2. maps와 같은 크기의 2차원 배열을 만들고 각 인덱스의 값은 해당 위치에 갈 수 있는 최솟값을 업데이트
3. maps의 값이 1인 부분만 지나갈 수 있음
*/
import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        Queue<int[]> q = new LinkedList<>();
        int[] dx = new int[]{-1,0,1,0};
        int[] dy = new int[]{0,1,0,-1};
        int n = maps.length;
        int m = maps[0].length;
        int[][] arr = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        for(int[] a : arr) Arrays.fill(a, Integer.MAX_VALUE);
        int ans = 0;
        
        q.offer(new int[]{0,0});
        arr[0][0] = 0;
        visited[0][0] = true;
        while(!q.isEmpty()) {
            int[] val = q.poll();
            int x = val[0]; int y = val[1];
            for(int d=0; d<4; d++) {
                int nx = x+dx[d];
                int ny = y+dy[d];
                if(nx>=0 && nx<n && ny>=0 && ny<m
                   && maps[nx][ny]==1 && !visited[nx][ny]) {
                    q.offer(new int[]{nx,ny});
                    visited[nx][ny] = true;
                    arr[nx][ny] = Math.min(arr[nx][ny], arr[x][y]+1);
                }
            }
        }
        
        
        if(arr[n-1][m-1]==Integer.MAX_VALUE) return -1;
        
        return arr[n-1][m-1]+1;
    }
}