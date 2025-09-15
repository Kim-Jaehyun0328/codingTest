import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Point {
        int x, y, dist, wall;
        Point(int a, int b, int c, int d) {
            x=a;
            y=b;
            dist=c;
            wall=d;
        }
    }

    static int N,M;
    static int[][] arr;
    static boolean[][][] visited; // [x][y][wall]
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int ans = 0;

    static int bfs(int sx, int sy, int ex, int ey) {
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(sx, sy,0,0));
        visited[sx][sy][0] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();

            if(p.x == ex && p.y == ey) return p.dist;

            for(int d=0; d<4; d++) {
                int nx = p.x + dx[d];
                int ny = p.y + dy[d];
                if(nx>=0 && nx<N && ny>=0 && ny<M) {
                    if(arr[nx][ny] == 0 && !visited[nx][ny][p.wall]) {
                        visited[nx][ny][p.wall] = true;
                        q.offer(new Point(nx,ny,p.dist+1, p.wall));
                    } else if(arr[nx][ny] == 1 && p.wall == 0 && !visited[nx][ny][1]) {
                        visited[nx][ny][1] = true;
                        q.offer(new Point(nx,ny, p.dist+1, 1));
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N][M][2];
        arr = new int[N][M];
        st = new StringTokenizer(br.readLine());
        int sx = Integer.parseInt(st.nextToken()) -1;
        int sy = Integer.parseInt(st.nextToken()) -1;
        st = new StringTokenizer(br.readLine());
        int ex = Integer.parseInt(st.nextToken()) -1;
        int ey = Integer.parseInt(st.nextToken()) -1;

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ans = bfs(sx,sy,ex,ey);
        System.out.println(ans);


    }
}
