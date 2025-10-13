class Solution {
    static char[] alphabet = new char[]{'A','E','I','O','U'};
    static int ans = 0;
    static boolean flag = false;
    static int seq = 0;
    
    public int solution(String word) {
        DFS(word, "");
        return ans;
    }
    
    private void DFS(String word, String s) {
        if(s.equals(word)) {
            ans = seq;
            flag = true;
            return;
        }
        if(!flag) {
            for(int i=0; i<5; i++) {
                if(s.length()<5) {
                    String temp = s+alphabet[i];
                    seq+=1;
                    DFS(word, temp);
                    temp = s;
                }
            }
        }
    }
    
}