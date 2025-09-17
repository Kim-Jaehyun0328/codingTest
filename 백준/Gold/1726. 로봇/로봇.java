import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Point {
        int x,y, dir, cnt;
        Point(int a, int b, int c, int d) {
            x=a;
            y=b;
            dir=c;
            cnt=d;
        }
    }
    static int M, N;
    static Point s;
    static int[][] arr;
    static int[][][] visited;

    static int[] dx = new int[]{0,0,0,1,-1};
    static int[] dy = new int[]{0,1,-1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new int[M][N];
        visited = new int[M][N][5];

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        int sx = Integer.parseInt(st.nextToken())-1;
        int sy = Integer.parseInt(st.nextToken())-1;
        int sdir = Integer.parseInt(st.nextToken());
        s = new Point(sx, sy, sdir,0);
        st = new StringTokenizer(br.readLine());
        int ex = Integer.parseInt(st.nextToken())-1;
        int ey = Integer.parseInt(st.nextToken())-1;
        int edir = Integer.parseInt(st.nextToken());

        Queue<Point> q = new LinkedList<>();
        q.offer(s);
        //visited[s.x][s.y][s.dir] = 0;
        while(!q.isEmpty()) {
            Point temp = q.poll();

            if(temp.x == ex && temp.y == ey && temp.dir == edir) {
                System.out.println(temp.cnt);
                return;
            }

            for(int k=1; k<=3; k++) {
                int nx = temp.x + dx[temp.dir] * k;
                int ny = temp.y + dy[temp.dir] * k;

                // 범위 & 벽 체크
                if(nx<0 || nx>=M || ny<0 || ny>=N || arr[nx][ny] == 1) break;

                if(visited[nx][ny][temp.dir] == 0) {
                    visited[nx][ny][temp.dir] =2;
                    q.offer(new Point(nx, ny, temp.dir, temp.cnt+1));
                }
            }

            int left = 0, right = 0, back = 0;

            switch(temp.dir) {
                case 1: left = 4; right = 3; back = 2; break;
                case 2: left = 3; right = 4; back = 1; break;
                case 3: left = 1; right = 2; back = 4; break;
                case 4: left = 2; right = 1; back = 3; break;
            }

            if(visited[temp.x][temp.y][left] == 0) {
                visited[temp.x][temp.y][left] = 2;
                q.add(new Point(temp.x,temp.y,left,temp.cnt+1));
            }

            if(visited[temp.x][temp.y][right] == 0) {
                visited[temp.x][temp.y][right] = 2;
                q.add(new Point(temp.x,temp.y,right,temp.cnt+1));
            }

            if(visited[temp.x][temp.y][back] == 0) {
                visited[temp.x][temp.y][back] = 2;
                q.add(new Point(temp.x,temp.y,back,temp.cnt+2));
            }
        }

    }
}
