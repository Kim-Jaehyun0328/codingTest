import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, K;
    static boolean[] visited = new boolean[100001];
    static int[][] ch = new int[100001][2];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        for(int i=0; i<=100000; i++) {
            ch[i][0] = Integer.MAX_VALUE;
        }
        visited[N] = true;
        ch[N][0] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.offer(N);

        while(!q.isEmpty()) {
            int pos = q.poll();

            if(pos==K) {
                System.out.println(ch[pos][0]);
                ArrayList<Integer> arr = new ArrayList<>();
                int temp = K;
                while (temp != N) {
                    arr.add(temp);
                    temp = ch[temp][1];
                }
                arr.add(N);
                Collections.reverse(arr);
                for (int x : arr) System.out.print(x + " ");
            }

            if(pos-1 > -1 && !visited[pos-1]) {
                ch[pos-1][0] = ch[pos][0] +1;
                ch[pos-1][1] = pos;
                visited[pos-1] = true;
                q.offer(pos-1);
            }
            if(pos + 1 < 100001 && !visited[pos+1]) {
                ch[pos+1][0] = ch[pos][0] +1;
                ch[pos+1][1] = pos;
                visited[pos+1] = true;
                q.offer(pos+1);
            }
            if(pos*2 < 100001 && !visited[pos*2]) {
                ch[pos*2][0] = ch[pos][0] +1;
                ch[pos*2][1] = pos;
                visited[pos*2] = true;
                q.offer(pos*2);
            }
        }
    }
}
