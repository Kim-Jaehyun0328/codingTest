import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {


    static int N, K;
    static int[] ch = new int[100001];
    static int ans = 0;
    static Queue<int[]> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        Arrays.fill(ch, Integer.MAX_VALUE);
        q.offer(new int[]{N, 0});
        ch[N] = 0;
        boolean flag = false;
        int min = Integer.MAX_VALUE;
        while(!q.isEmpty()) {
            //temp는 현재 위치를 나타냄
            int[] temp = q.poll();
            //최소값이 나왔다면
//            if (temp[0] == K) {
//                if (temp[1] < min) {
//                    min = temp[1];
//                    ans = 1;
//                } else if (temp[1] == min) {
//                    ans++;
//                }
//            }

            if(temp[0] == K) {
                if(!flag) {
                    flag = true;
                    min = temp[1];
                    ans++;
                } else {
                    if(min == temp[1]) ans++;
                }
            }
            int pos = temp[0], sec = temp[1];
            if (pos-1 >= 0 && ch[pos - 1] >= sec + 1) {
                ch[pos - 1] = sec + 1;
                q.offer(new int[]{pos - 1, sec + 1});
            }
            if (pos+1 < 100001 && ch[pos + 1] >= sec + 1) {
                ch[pos + 1] = sec + 1;
                q.offer(new int[]{pos + 1, sec + 1});
            }
            if (pos*2 < 100001 && ch[pos * 2] >= sec + 1) {
                ch[pos * 2] = sec + 1;
                q.offer(new int[]{pos * 2, sec + 1});
            }
        }

        System.out.println(min);
        System.out.println(ans);
    }
}
