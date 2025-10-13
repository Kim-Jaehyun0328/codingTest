import java.util.*;

class Solution {
    static int[][] arr;
    static int ans = Integer.MAX_VALUE;
    public int solution(int n, int[][] wires) {
        arr = new int[n+1][n+1];
        for(int i=0; i<wires.length; i++) {
            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }
        
        DFS(wires);
        return ans;
    }
    
    private void DFS(int[][] wires) {
        for(int i=0; i<wires.length; i++) {
            arr[wires[i][0]][wires[i][1]] = 0;
            arr[wires[i][1]][wires[i][0]] = 0;
            find();
            arr[wires[i][0]][wires[i][1]] = 1;
            arr[wires[i][1]][wires[i][0]] = 1;
        }
    }
    
    private void find() {
        Set<Integer> set = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        set.add(1);
        q.add(1);
        boolean[] checked = new boolean[arr.length];
        checked[1] = true;
        while(!q.isEmpty()) {
            int num = q.poll();
            for(int i=1; i<arr.length; i++) {
                if(arr[num][i]==1 && !checked[i]) {
                    q.offer(i);
                    set.add(i);
                    checked[i] = true;
                }
            }
        }
        int tot = arr.length-1;
        int temp = Math.abs(set.size()-tot);
        ans = Math.min(ans, Math.abs(temp-set.size()));
    }
    
}