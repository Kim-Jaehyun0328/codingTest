import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class State {
        int rx, ry, bx, by, depth;
        State(int a, int b, int c, int d, int e) {
            rx=a;
            ry=b;
            bx=c;
            by=d;
            depth=e;
        }
    }

    static class Point {
        int x, y, dist;
        Point(int a, int b, int c) {
            x=a;
            y=b;
            dist=c;
        }
    }

    static Point roll(int x, int y, int dx, int dy) {
        int dist = 0;
        while(board[x+dx][y+dy] != '#' && board[x][y] != 'O') {
            x += dx;
            y += dy;
            dist++;
        }
        return new Point(x,y,dist);
    }

    static int N,M;
    static char[][] board;
    static boolean[][][][] visited;
    static int[][][][] ch;

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        visited = new boolean[N][M][N][M];
        ch = new int[N][M][N][M];
        int rx=0, ry=0, bx=0, by =0;
        for(int i=0; i<N; i++) {
            String temp = br.readLine();
            for(int j=0; j<M; j++){
                char c = temp.charAt(j);
                board[i][j] = c;
                if(c == 'R') {
                    rx=i;
                    ry=j;
                } else if(c == 'B') {
                    bx=i;
                    by=j;
                }
            }
        }
        visited[rx][ry][bx][by] = true;
        Queue<State> q = new LinkedList<>();
        q.offer(new State(rx,ry,bx,by,0));

        while(!q.isEmpty()) {
            State state = q.poll();
            if(state.depth >= 10) continue;

            for(int d=0; d<4; d++) {
                Point red = roll(state.rx, state.ry, dx[d], dy[d]);
                Point blue = roll(state.bx, state.by, dx[d], dy[d]);

                if(board[blue.x][blue.y] == 'O') continue;
                if(board[red.x][red.y] == 'O') {
                    System.out.println(state.depth+1);
                    return;
                }

                if(red.x == blue.x && red.y == blue.y) {
                    if(red.dist > blue.dist) {
                        red.x -= dx[d];
                        red.y -= dy[d];
                    } else {
                        blue.x -= dx[d];
                        blue.y -= dy[d];
                    }
                }

                if(!visited[red.x][red.y][blue.x][blue.y]) {
                    visited[red.x][red.y][blue.x][blue.y] = true;
                    q.offer(new State(red.x, red.y, blue.x, blue.y, state.depth+1));
                }

            }
        }


        System.out.println(-1);
    }
}
