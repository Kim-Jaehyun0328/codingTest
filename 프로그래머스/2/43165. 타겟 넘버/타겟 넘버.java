//1. DFS 활용
//2. +, - 돌아가면서 DFS호출
//3. cnt값이 numbers.length와 같으면 target과 같은지 비교

class Solution {
    
    static int ans = 0;
    
    public int solution(int[] numbers, int target) {
        DFS(numbers, target, 0, 0, 0);
        return ans;
    }
    
    private void DFS(int[] numbers, int target, int idx, int cnt, int num) {
        if(numbers.length==cnt && target==num) ans++;
        else {
            for(int i=idx; i<numbers.length; i++) {
                DFS(numbers, target, i+1, cnt+1, num+numbers[i]);
                DFS(numbers, target, i+1, cnt+1, num-numbers[i]);
            }
        }
    }
    
}