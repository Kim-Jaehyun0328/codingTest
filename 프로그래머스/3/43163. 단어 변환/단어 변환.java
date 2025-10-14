class Solution {
    
    static boolean[] visited;
    static int ans = 0;
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        int answer = 0;
        boolean flag = false;
        for(String word : words) {
            if(word.equals(target)) {
                flag = true;
                break;
            }
        }
        //words에 target 단어가 없으면 종료
        if(!flag) return 0;
        
        DFS(0, begin, target, words);
        
        
        return ans;
    }
    
    
    private int DFS(int cnt, String s, String target, String[] words) {
        if(s.equals(target)) {
            ans = cnt;
            return cnt;
        }
        for(int i=0; i<words.length; i++) {
            if(!visited[i]) {
                int same = 0;
                for(int j=0; j<words[i].length(); j++) {
                    if(s.charAt(j)==words[i].charAt(j)) {
                        same++;
                    }
                }
                //한 글자만 다른 거라면
                if(same==s.length()-1) {
                    visited[i] = true;
                    DFS(cnt+1, words[i], target, words);
                    visited[i] = false;
                }
            }
        }
        return 0;
    }
}