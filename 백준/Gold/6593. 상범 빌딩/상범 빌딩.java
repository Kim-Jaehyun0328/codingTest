import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int L, R, C;

    static char[][][] arr;
    static boolean[][][] visited;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static boolean flag = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            L = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            if(L==0 && R==0 && C==0) return;
            Queue<int[]> q = new LinkedList<>();
            arr = new char[L][R][C];
            visited = new boolean[L][R][C];
            for(int l=0; l<L; l++) {
                for(int i=0; i<R; i++) {
                    String temp = br.readLine();
                    for(int j=0; j<C; j++) {
                        arr[l][i][j] = temp.charAt(j);
                        if(arr[l][i][j] == 'S') {
                            q.offer(new int[]{l,i,j, 0});
                            visited[l][i][j] = true;
                        }
                    }
                }
                br.readLine();
            }
            int ans = -1;
            flag = false;
            while(!q.isEmpty()) {
                int[] cur = q.poll();
                int z = cur[0], x = cur[1], y = cur[2], dist = cur[3];

                if (arr[z][x][y] == 'E') {
                    System.out.println("Escaped in " + dist + " minute(s).");
                    flag = true;
                    break;
                }

                // 6방향 탐색
                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx >= 0 && nx < R && ny >= 0 && ny < C
                            && !visited[z][nx][ny] && arr[z][nx][ny] != '#') {
                        visited[z][nx][ny] = true;
                        q.offer(new int[]{z, nx, ny, dist + 1});
                    }
                }
                if (z > 0 && !visited[z-1][x][y] && arr[z-1][x][y] != '#') {
                    visited[z-1][x][y] = true;
                    q.offer(new int[]{z-1, x, y, dist + 1});
                }
                if (z < L-1 && !visited[z+1][x][y] && arr[z+1][x][y] != '#') {
                    visited[z+1][x][y] = true;
                    q.offer(new int[]{z+1, x, y, dist + 1});
                }
            }
            if(!flag) System.out.println("Trapped!");
        }



    }
}