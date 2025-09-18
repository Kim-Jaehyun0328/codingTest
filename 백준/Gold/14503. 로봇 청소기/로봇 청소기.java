import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class Position {
        int x,y,dir;
        Position(int a,int b, int c) {
            x=a; y=b; dir=c;
        }
    }
    static int N,M;
    static int[][] arr;
    static Position now;
    static Queue<Position> q = new LinkedList<>();

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        st = new StringTokenizer(br.readLine());
        now = new Position(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs();
        System.out.println(ans);
    }

    static void bfs() {
        q.offer(now);

        while(true) {
            Position p = q.poll();
            if(arr[p.x][p.y] == 0) {
                arr[p.x][p.y] = 2;
                ans++;
            }
            boolean flag = false;
            for(int d=0; d<4; d++) {
                int nx = p.x + dx[d];
                int ny = p.y + dy[d];
                //사방에서 청소할 곳이 있다면 flag는 true
                if(inRoom(nx, ny) && arr[nx][ny] == 0) {
                    flag = true;
                    break;
                }
            }
            //사방에 청소할 곳이 없다면 뒤로 후진
            if(!flag) {
                //뒤가 벽이라면 종료, 뒤로 갈 수 있으면 후진하고 q에 새로 추가 (방향은 그대로)
                int idx = 0;
                switch (p.dir) {
                    case 0: idx=2; break;
                    case 1: idx=3; break;
                    case 2: idx=0; break;
                    case 3: idx=1; break;
                }
                int bx = p.x + dx[idx];
                int by = p.y + dy[idx];
                //뒤로 후진할 수 있다면
                if(inRoom(bx, by) && arr[bx][by] != 1) {
                    q.offer(new Position(bx, by, p.dir));
                } else break;
            } else { //사방 중에 청소할 곳이 있다면 반시계로 90도 회전
                int dir = rotate(p.dir);
                int fx = p.x + dx[dir];
                int fy = p.y + dy[dir];
                //반시계 회전 후 앞에가 청소해야 할곳이라면 이동
                if(inRoom(fx, fy) && arr[fx][fy]==0) {
                    q.offer(new Position(fx,fy, dir));
                } else {
                    q.offer(new Position(p.x, p.y, dir));
                }
            }
        }
    }

    static boolean inRoom(int nx, int ny) {
        return nx>=0 && nx<N && ny>=0 && ny<M;
    }

    static int rotate(int dir) {
        dir -= 1;
        if(dir<0) dir = 3;
        return dir;
    }
}
