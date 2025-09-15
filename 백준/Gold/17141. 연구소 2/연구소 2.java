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
    static int ans = Integer.MAX_VALUE;
    static boolean flag = false;

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};

    static void bfs() {
        int cnt = 0;
        Queue<int[]> q = new LinkedList<>();
        boolean[][] arrTemp = new boolean[N][N];


        //index 값이 3인 위치를 큐에 추가
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(arr[i][j] == 3) {
                    q.add(new int[]{i,j,0});
                    cnt++;
                    arrTemp[i][j] = true;
                }
            }
            if(cnt==M) break;
        }

        int temp = 0;
        while(!q.isEmpty()) {
            int[] poll = q.poll();
            for(int d=0; d<4; d++) {
                int nx = poll[0] + dx[d];
                int ny = poll[1] + dy[d];
                if(nx>=0 && nx<N && ny>=0 && ny<N && !arrTemp[nx][ny] && arr[nx][ny] != 1) {
                    //if(arr[nx][ny] == 0) {
                        temp = Math.max(temp, poll[2] + 1); // 빈칸일 때만 시간 갱신
                    //}
                    arrTemp[nx][ny] = true; // 방문 처리 (시간 대신 마킹만)
                    q.offer(new int[]{nx, ny, poll[2]+1});
                }
            }
        }


        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if(arr[i][j] == 0 && !arrTemp[i][j]) return;
                else if(arr[i][j] == 2 && !arrTemp[i][j]) return;
            }
        }
        flag = true;
        ans = Math.min(ans, temp);


    }

    static void dfs(int start, int depth) {
        if(depth == M) {
            //bfs
            bfs();
        } else {
            for(int i=start; i<virus.size(); i++) {
                //바이러스를 둘 수 있는 인덱스 정보
                int[] v = virus.get(i);
                arr[v[0]][v[1]] = 3;
                dfs(i+1, depth+1);
                arr[v[0]][v[1]] = 2;
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
