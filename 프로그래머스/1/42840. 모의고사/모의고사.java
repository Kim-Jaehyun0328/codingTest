//1번의 정답은 idx%5+1

//2번의 정답은 짝수는 무조건 2, 홀수는 +8마다 1,3,4,5가 반복됨
//idx%8 값이 1이면 1, 3이면 3, 5면 4, 7이면 5

//3번의 정답은 10마다 반복
//크기 10인 배열 만들어서 idx%10 값이 정답

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] cnt = new int[3];
        
        int[] three = new int[]{3,3,1,1,2,2,4,4,5,5};
        
        for(int i=0; i<answers.length; i++) {
            //1번 수포자 정답 처리
            if(answers[i] == i%5+1) cnt[0] += 1;
            
            //2번 수포자 정답 처리
            if(i%2==0 && answers[i]==2) cnt[1] += 1;
            else if(answers[i]==1 && i%8==1) cnt[1] += 1;
            else if(answers[i]==3 && i%8==3) cnt[1] += 1;
            else if(answers[i]==4 && i%8==5) cnt[1] += 1;
            else if(answers[i]==5 && i%8==7) cnt[1] += 1;
            
            //3번 수포자 정답 처리
            if(answers[i] == three[i%10]) cnt[2] += 1;
        }
        
        int max = Integer.MIN_VALUE;
        List<Integer> arr = new ArrayList<>();
        for(int c: cnt) {
            max = Math.max(max, c);
        }
        
        for(int i=0; i<cnt.length; i++) {
            if(max == cnt[i]) arr.add(i+1);
        }
        
        
        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
}