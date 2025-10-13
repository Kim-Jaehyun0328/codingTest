//1. DFS로 dep==numbers.length()까지 조합
//2. 해당 문자열을 숫자로 변경 -> Integer.parseInt() -> 소수 판별
//3. DFS(numbers, dep)
//static 변수로 chedked 배열 필요?

import java.util.*;
class Solution {
    static int answer = 0;
    static boolean[] checked;
    static Set<Integer> set = new HashSet<>();
    
    public int solution(String numbers) {
        checked = new boolean[numbers.length()];
        DFS(numbers.toCharArray(), "");
        return set.size();
    }
    
    private void DFS(char[] numbers, String temp) {
        //소수 확인
        check(temp);
        //숫자조합
        for(int i=0; i<numbers.length; i++) {
            if(!checked[i]) {
                String s = temp+numbers[i];
                checked[i] = true;
                DFS(numbers, s);
                checked[i] = false;
            }
        }
    }
    
    //1. 빈 문자열인지 확인
    //2. 0이면 return
    private void check(String temp) {
        if("".equals(temp)) return;
        int num = Integer.parseInt(temp);
        if(num==1 || num==0) return;
        else if(num==2) {
            set.add(num);
            return;
        }
        for(int i=2; i<=Math.sqrt(num); i++) {
            if(num%i==0) return;
        }
        set.add(num);
    }
    
}