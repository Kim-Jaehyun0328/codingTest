
// /*
// 1. n+1 크기를 가진 2차원 배열 생성 -> 간선 정보 초기화
// 2. 1에서부터 거리 정보를 가질 n+1크기의 1차원 배열 생성
// 2. q를 활용
// */
// import java.util.*;
// class Solution {
//     public int solution(int n, int[][] edge) {
//         int answer = 0;
//         int[][] arr = new int[n+1][n+1];
//         int[] dist = new int[n+1];
//         boolean[] visited = new boolean[n+1];
        
//         for(int[] e : edge) {
//             arr[e[0]][e[1]] = 1;
//             arr[e[1]][e[0]] = 1;
//         }
        
//         Queue<Integer> q = new LinkedList<>();
//         //1과 연결된 노드들은 미리 초기화를 한다.
//         visited[1] = true;
//         for(int i=2; i<n+1; i++) {
//             if(arr[1][i]==1) {
//                 q.add(i);
//                 dist[i] = 1;
//                 visited[i] = true;
//             }
//         }
        
//         //가장 멀리 떨어진 값 초기화 필요
//         int max = Integer.MIN_VALUE;
//         while(!q.isEmpty()) {
//             int v = q.poll();
//             for(int i=2; i<n+1; i++) {
//                 if(arr[v][i]==1 && !visited[i]) {
//                     dist[i] = dist[v]+1;
//                     visited[i] = true;
//                     q.offer(i);
//                     max = Math.max(max, dist[i]);
//                 }
//             }
//         }
        
//         for(int d : dist) {
//             if(d==max) answer++;
//         }
        
//         return answer;
//     }
// }



/*
1. n+1 크기를 가진 2차원 배열 생성 -> 간선 정보 초기화
2. 1에서부터 거리 정보를 가질 n+1크기의 1차원 배열 생성
2. q를 활용
*/
import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        int[] dist = new int[n+1];
        boolean[] visited = new boolean[n+1];
        
        for(int i=0; i<=n; i++) arr.add(new ArrayList<>());
        
        for(int[] e : edge) {
            arr.get(e[0]).add(e[1]);
            arr.get(e[1]).add(e[0]);
        }
        
        Queue<Integer> q = new LinkedList<>();
        //1과 연결된 노드들은 미리 초기화를 한다.
        visited[1] = true;
        for(int v : arr.get(1)) {
            visited[v] = true;
            dist[v] = 1;
            q.offer(v);
        }
        
        //가장 멀리 떨어진 값 초기화 필요
        int max = Integer.MIN_VALUE;
        while(!q.isEmpty()) {
            int v = q.poll();
            for(int num : arr.get(v)) {
                if(!visited[num]) {
                    q.offer(num);
                    dist[num] = dist[v]+1;
                    visited[num] = true;
                    max = Math.max(max, dist[num]);
                }
            }
        }
        
        for(int d : dist) {
            if(d==max) answer++;
        }
        
        return answer;
    }
}