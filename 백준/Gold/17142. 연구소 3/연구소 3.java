import javax.print.attribute.standard.QueuedJobCount;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] arr;
    static ArrayList<int[]> virus = new ArrayList<>();
    static int ans = Integer.MAX_VALUE;
    static boolean flag = false;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};

    static void bfs() {
        boolean[][] visited = new boolean[N][N];
        Queue<int[]> q = new LinkedList<>();
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(arr[i][j] == 3) {
                    q.offer(new int[]{i,j,0});
                    visited[i][j] = true;
                }
            }
        }

        int sec = 0;
        while(!q.isEmpty()) {
            for(int i=0; i<q.size(); i++) {
                int[] temp = q.poll();
                for(int d=0; d<4; d++) {
                    int nx = temp[0] + dx[d];
                    int ny = temp[1] + dy[d];
                    if(nx>=0 && nx<N && ny>=0 && ny<N && arr[nx][ny] != 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        if(arr[nx][ny] == 0) sec = Math.max(sec, temp[2] +1);
                        q.offer(new int[]{nx,ny, temp[2]+1});
                    }
                }
            }
        }

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(arr[i][j] == 0 && !visited[i][j]) return;
            }
        }
        flag = true;
        ans = Math.min(ans, sec);

    }

    static void dfs(int start, int depth) {
        if(depth == M) {
            bfs();
        } else {
            for(int i=start; i<virus.size(); i++) {
                int[] temp = virus.get(i);
                arr[temp[0]][temp[1]] = 3;
                dfs(i+1, depth+1);
                arr[temp[0]][temp[1]] = 2;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[i][j] = num;
                if(num == 2) virus.add(new int[]{i,j});
            }
        }


        dfs(0,0);

        if(flag) System.out.println(ans);
        else System.out.println(-1);
    }
}
