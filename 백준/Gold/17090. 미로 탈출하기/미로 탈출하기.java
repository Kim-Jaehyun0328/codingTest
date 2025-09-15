import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N,M;
    static char[][] arr;
    static boolean[][] visited;
    static int ans = 0;
    static int[][] ch;

    static int dfs(int x,int y) {
        //탈출 성공하면 1반환
        if(x<0 || x>=N || y<0 || y>=M) return 1;

        //결과가 정해진 칸이라면 해당 값 반환 0: 미방문, 1: 탈출 가능, -1: 탈출 불가능(순환)
        if(ch[x][y] != 0) return ch[x][y];

        //방문한 곳이라면 -1처리
        if(visited[x][y]) return ch[x][y] = -1;

        //첫 방문이라면 방문처리
        visited[x][y] = true;

        int nx=x, ny=y;
        char c = arr[x][y];
        if(c=='U') nx-=1;
        else if(c=='R') ny+=1;
        else if(c=='D') nx+=1;
        else if(c=='L') ny-=1;

        ch[x][y] = dfs(nx, ny);
        visited[x][y] = false;

        return ch[x][y];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new char[N][M];
        visited = new boolean[N][M];
        ch = new int[N][M];
        for(int i = 0; i < N; i++) {
            String str = br.readLine();
            for(int j=0; j<M; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                if(dfs(i,j) == 1) ans++;
            }
        }

        System.out.println(ans);
    }
}
