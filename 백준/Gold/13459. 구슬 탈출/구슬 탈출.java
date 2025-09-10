import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static char[][] arr;
    static int[] pos = new int[5];
    static int[] hole = new int[2];
    static boolean[][][][] visited;
    static int N,M;

    static int[] roll(int x, int y, int dx, int dy) {
        int dist = 0;
        while(arr[x+dx][y+dy] != '#' && arr[x][y] !='O') {
            x += dx;
            y += dy;
            dist++;
        }
        return new int[]{x, y, dist};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new char[N][M];
        visited = new boolean[N][M][N][M];
        for(int i=0; i<N; i++) {
            String temp = br.readLine();
            for(int j=0; j<M; j++) {
                arr[i][j] = temp.charAt(j);
                if(arr[i][j] == 'R') {
                    pos[0] = i;
                    pos[1] = j;
                } else if(arr[i][j] == 'B') {
                    pos[2] = i;
                    pos[3] = j;
                } else if(arr[i][j] == 'O') {
                    hole[0] = i;
                    hole[1] = j;
                }
            }
        }

        Queue<int[]> q =new LinkedList<>();
        q.offer(pos);
        visited[pos[0]][pos[1]][pos[2]][pos[3]] = true;
        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int rx = temp[0], ry = temp[1], bx = temp[2], by = temp[3], cnt = temp[4];
            if (cnt >= 10) continue;
            for(int d=0; d<4; d++) {
                //0은 x, 1은 y, 2는 dist
                int[] red = roll(rx, ry, dx[d], dy[d]);
                int[] blue = roll(bx, by, dx[d], dy[d]);
                if (arr[blue[0]][blue[1]] == 'O') continue;
                if (arr[red[0]][red[1]] == 'O') {
                    System.out.println(1);
                    return;
                }
                if(red[0] == blue[0] && red[1] == blue[1]) {
                    if(red[2] > blue[2]) {
                        red[0] -= dx[d];
                        red[1] -= dy[d];
                    } else {
                        blue[0] -= dx[d];
                        blue[1] -= dy[d];
                    }
                }
                if(!visited[red[0]][red[1]][blue[0]][blue[1]]) {
                    visited[red[0]][red[1]][blue[0]][blue[1]] = true;
                    q.offer(new int[]{red[0], red[1], blue[0], blue[1], cnt+1});
                }
            }
        }

        System.out.println(0);
    }
}
