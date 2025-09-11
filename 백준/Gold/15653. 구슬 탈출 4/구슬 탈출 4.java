import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class State {
        int rx,ry,bx,by,depth;
        State(int a, int b, int c, int d, int e){
            rx=a;
            ry=b;
            bx=c;
            by=d;
            depth=e;
        }
    }
    static int N, M;
    static char[][] board;
    static boolean[][][][] visited;

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};

    static int[] roll(int x, int y, int dx, int dy) {
        int dist = 0;
        while(board[x+dx][y+dy] != '#' && board[x][y] != 'O') {
            x += dx;
            y += dy;
            dist++;
        }
        return new int[]{x,y,dist};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        visited = new boolean[N][M][N][M];
        int rx=0, ry=0, bx=0, by=0;
        for(int i=0; i<N; i++) {
            String temp = br.readLine();
            for(int j=0; j<M; j++) {
                char c = temp.charAt(j);
                board[i][j] = c;
                if(c == 'R') {
                    rx=i;
                    ry=j;
                }
                if(c == 'B') {
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
            for(int d=0; d<4; d++) {
                //인덱스 0은 x, 1은 y, 2는 이동 거리
                int[] red = roll(state.rx, state.ry, dx[d], dy[d]);
                int[] blue = roll(state.bx, state.by, dx[d], dy[d]);

                if(board[blue[0]][blue[1]] == 'O') continue;
                if(board[red[0]][red[1]] == 'O') {
                    System.out.println(state.depth+1);
                    return;
                }

                if(red[0]==blue[0] && red[1]==blue[1]) {
                    if(red[2] > blue[2]) {
                        red[0] -= dx[d];
                        red[1] -= dy[d];
                    } else {
                        blue[0] -= dx[d];
                        blue[1] -= dy[d];
                    }
                }
                if(!visited[red[0]][red[1]][blue[0]][blue[1]]) {
                    visited[red[0]][red[1]][blue[0]][blue[1]] =true;
                    q.offer(new State(red[0], red[1], blue[0], blue[1], state.depth+1));
                }
            }
        }

        System.out.println(-1);
    }
}
