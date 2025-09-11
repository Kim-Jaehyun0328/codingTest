import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static boolean[] ch = new boolean[1000000];
    static int[][] arr = new int[5][5];
    static int ans = 0;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static void dfs(int x, int y, int depth, String temp) {
        if(depth==6) {
            int num = Integer.parseInt(temp);
            if(!ch[num]) {
                ans++;
                ch[num] = true;
            }
        } else {
            for(int d=0; d<4; d++) {
                int nx = x+dx[d];
                int ny = y+dy[d];
                if(nx>=0 && nx<5 && ny>=0 && ny<5) {
                    dfs(nx,ny,depth+1, temp+(arr[nx][ny]));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for(int i=0; i<5; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<5; j++) {
                 arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                dfs(i,j,1, String.valueOf(arr[i][j]));
            }
        }
        System.out.println(ans);
    }
}
