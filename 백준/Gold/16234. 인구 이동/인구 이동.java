
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N,L,R;
    static int[][] arr;
    static boolean[][] ch;
    static Queue<int[]> q = new LinkedList<>();

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        ch = new boolean[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        process();
        System.out.println(ans);
    }

    static void process(){
        while(true) {
            ch = new boolean[N][N];
            boolean flag = false;
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    //아직 이번 회차에서 방문하지 않았다면
                    if(!ch[i][j]) {
                        ch[i][j] = true;
                        q.offer(new int[]{i,j});
                        ArrayList<int[]> union = new ArrayList<>();
                        union.add(new int[]{i,j});
                        while(!q.isEmpty()) {
                            int[] temp = q.poll();
                            for(int d=0; d<4; d++) {
                                int nx = temp[0]+dx[d];
                                int ny = temp[1]+dy[d];
                                //옆 칸이 L,R 사이이고 방문하지 않았다면
                                if(inRoom(nx, ny) && !ch[nx][ny]) {
                                    int num = Math.abs(arr[temp[0]][temp[1]]-arr[nx][ny]);
                                    if(num>=L && num<=R) {
                                        q.offer(new int[]{nx,ny});
                                        union.add(new int[]{nx,ny});
                                        ch[nx][ny] = true;
                                    }
                                }
                            }
                        }
                        //하나의 연합이 생겼다면
                        if (union.size() > 1) {
                            union(union);
                            flag = true;
                        }
                    }
                }
            }
            if(!flag) break;
            else ans++;
        }

    }

    static boolean inRoom(int x, int y) {
        return (x>=0 && x<N && y>=0 && y<N);
    }

    static void union(ArrayList<int[]> union) {
        int tot = 0;
        int n = union.size();
        for (int[] ints : union) {
            tot+=arr[ints[0]][ints[1]];
        }

        int div = (tot/n);
        for (int[] ints : union) {
            arr[ints[0]][ints[1]] = div;
        }

    }


}
