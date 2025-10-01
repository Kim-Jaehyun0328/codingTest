import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static class Info implements Comparable<Info> {
        int idx, age;
        String name;
        Info(int a, int b, String c) {
            idx=a; age=b; name=c;
        }
        @Override
        public int compareTo(Info o) {
            if(this.age==o.age) return this.idx-o.idx;
            return this.age-o.age;
        }
    }

    static int N;
    static ArrayList<Info> arr = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            arr.add(new Info(i,age, name));
        }
        Collections.sort(arr);
        for(Info i:arr) {
            System.out.print(i.age + " " + i.name);
            System.out.println();
        }
    }
}
