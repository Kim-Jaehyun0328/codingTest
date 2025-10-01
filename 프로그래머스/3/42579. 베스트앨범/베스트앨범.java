import java.util.*;

class Type implements Comparable<Type>{
    int index;
    int plays;
    
    Type(int a, int b) {
        index=a; plays=b;
    }
    @Override
    public int compareTo(Type o) {
        if(o.plays==this.plays) return this.index-o.index;
        return o.plays-this.plays;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        HashMap<String, ArrayList<Type>> map = new HashMap<>();
        HashMap<String, Integer> most = new HashMap<>();
        
        //most, map에 값 추가
        for(int i=0; i<genres.length; i++) {
            most.put(genres[i],most.getOrDefault(genres[i],0) + plays[i]);
            map.putIfAbsent(genres[i], new ArrayList<>());
            map.get(genres[i]).add(new Type(i, plays[i]));
        }
        
        
        ArrayList<Integer> temp = new ArrayList<>();
        ArrayList<String> genreList = new ArrayList<>(most.keySet());
        genreList.sort((a, b) -> most.get(b) - most.get(a));
        
        for(String entry : genreList) {
            String key = entry;
            ArrayList<Type> arr = map.get(key);
            Collections.sort(map.get(key));
            temp.add(arr.get(0).index);
            if(arr.size()>1) temp.add(arr.get(1).index);
        }
        answer = new int[temp.size()];
        for(int i=0; i<temp.size(); i++) {
            answer[i] = temp.get(i);
        }
        
        return answer;
    }
}