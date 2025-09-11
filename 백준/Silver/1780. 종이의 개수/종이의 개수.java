import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[][] arr;
    static int[] ans = new int[3];

    static void dfs(int x, int y, int size) {
        int first = arr[x][y];
        boolean same = true;

        // 현재 블록이 모두 같은 값인지 검사
        for (int i=x; i<x+size; i++) {
            for (int j=y; j<y+size; j++) {
                if (arr[i][j] != first) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
        }

        if (same) {
            // 모두 같은 값이라면 해당 값 카운트
            ans[first+1]++;
        } else {
            // 다르면 9등분해서 재귀 호출
            int newSize = size/3;
            for (int i=0; i<3; i++) {
                for (int j=0; j<3; j++) {
                    dfs(x + i*newSize, y + j*newSize, newSize);
                }
            }
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[i][j] = num;
            }
        }

       dfs(0,0,N);


        for (int an : ans) {
            System.out.println(an);
        }


    }
}
