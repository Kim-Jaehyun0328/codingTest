class Solution {
    public int[] solution(int brown, int yellow) {
        int sum = brown + yellow;
        int[] ans = new int[]{sum, 1};
        
        int cnt=0;
        while(true) {
            int mul = ans[0]*ans[1];
            if(mul==sum) {
                int b = (ans[0]*2) + ((ans[1]-2)*2);
                int y = (ans[0]-2) * (ans[1]-2);
                if(b==brown && yellow==y) break;
            }
            ans[1]++;
            ans[0] = sum/ans[1];
            cnt++;
        }
        return ans;
    }
}