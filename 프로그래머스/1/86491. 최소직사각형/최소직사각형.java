import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int h = Integer.MIN_VALUE;
        int w = Integer.MIN_VALUE;
        for(int[] size: sizes) {
            Arrays.sort(size);
            if(h < size[0]) h = size[0];
            if(w < size[1]) w = size[1];
        }
        
        return h*w;
    }
}