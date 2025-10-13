import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int h = Integer.MIN_VALUE;
        int w = Integer.MIN_VALUE;
        for(int[] size: sizes) {
            Arrays.sort(size);
            h = Math.max(h, size[0]);
            w = Math.max(w, size[1]);
        }
        
        return h*w;
    }
}