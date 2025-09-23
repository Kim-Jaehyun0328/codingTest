
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int R,C,N;
    static char[][] arr;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        arr = new char[R][C];
        for(int i=0; i<R; i++) {
            String str = br.readLine();
            for(int j=0; j<C; j++) {
                char c = str.charAt(j);
                arr[i][j] = c;
            }
        }

        if(N==1) print(arr);
        else if(N%2==0) {
            fillBomb();
            print(arr);
        } else {
            char[][] afterFirstBoom = boom(arr);
            char[][] afterSecondBoom = boom(afterFirstBoom);

            if (N % 4 == 3) print(afterFirstBoom);
            else print(afterSecondBoom); // N % 4 == 1
        }

    }



    static char[][] boom(char[][] map) {
        char[][] next = new char[R][C];
        for(int i=0; i<R; i++) Arrays.fill(next[i], 'O');

        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if(map[i][j] == 'O') {
                    next[i][j] = '.';
                    for(int d=0; d<4; d++) {
                        int nx = i+dx[d], ny=j+dy[d];
                        if(inRoom(nx,ny)) next[nx][ny] = '.';
                    }
                }
            }
        }
        return next;
    }

    static void fillBomb() {
        for(int i=0; i<R; i++) Arrays.fill(arr[i], 'O');
    }

    static boolean inRoom(int x, int y) {
        return (x>=0 && x<R && y>=0 && y<C);
    }

    static void print(char[][] board) {
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println();
        }
    }

}
