import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N, M;
    static int[][] arr;
    static ArrayList<int[]> virus = new ArrayList<>();

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = 0;

    static void bfs() {
        int[][] arrTemp = new int[N][M];
        for (int i = 0; i < N; i++) arrTemp[i] = arr[i].clone();
        for (int[] ints : virus) {
            Queue<int[]> q = new LinkedList<>();
            q.offer(ints);
            while(!q.isEmpty()) {
                int[] temp = q.poll();
                for(int d=0; d<4; d++) {
                    int nx = temp[0] + dx[d];
                    int ny = temp[1] + dy[d];
                    if(nx>=0 && nx<N && ny>=0 && ny<M && arrTemp[nx][ny] == 0) {
                        arrTemp[nx][ny] = 2;
                        q.offer(new int[]{nx,ny});
                    }
                }
            }
        }
        int temp = 0;
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(arrTemp[i][j] == 0) temp++;
            }
        }
        ans = Math.max(ans, temp);
    }

    static void dfs(int x, int y, int depth) {
        //벽 3개 다 세움
        if(depth==3) {
            bfs();
        } else {
            for(int i=x; i<N; i++) {
                for(int j=0; j<M; j++) {
                    //방문하지 않은 빈 공간이라면
                    if(arr[i][j] == 0) {
                        arr[i][j] = 1;
                        dfs(i,j, depth+1);
                        arr[i][j] = 0;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[i][j] = num;
                if(num ==2) virus.add(new int[]{i,j});
            }
        }

        dfs(0,0,0);
        System.out.println(ans);


    }
}
