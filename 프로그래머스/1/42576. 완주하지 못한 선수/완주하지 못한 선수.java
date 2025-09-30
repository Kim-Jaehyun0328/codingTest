import java.util.*;


//완주한 선수 목록을 map에 추가
//참가 선수 목록 반복문으로 돌려 map에 없는 선수 추출
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();
        for(int i=0; i<completion.length; i++) {
            map.put(completion[i], map.getOrDefault(completion[i],0)+1);
        }
        
        for(int i=0; i<participant.length; i++) {
            Integer a = map.get(participant[i]);
            if(a==null) return participant[i];
            map.put(participant[i], a-1);
        }
        for(String name : map.keySet()) {
            if(map.get(name) == -1) return name;
        }
        return "";
    }
}