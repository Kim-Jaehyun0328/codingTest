import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {


    static class Point {
        int x, y;
        Point(int a, int b) {
            x=a;
            y=b;
        }
    }

    static int N;
    static int[][] arr;
    static boolean[][] ch;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = Integer.MIN_VALUE;
    static int temp = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        ch = new boolean[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        Queue<Point> q = new LinkedList<>();
        for(int h=0; h<=100; h++) {
            for(int a=0; a<N; a++) Arrays.fill(ch[a], false);
            temp = 0;
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if(arr[i][j] > h && !ch[i][j]) {
                        q.offer(new Point(i,j));
                        temp+=1;
                        while(!q.isEmpty()) {
                            Point temp = q.poll();
                            for(int d=0; d<4; d++) {
                                int nx = dx[d] + temp.x;
                                int ny = dy[d] + temp.y;
                                if(nx>=0 && nx<N && ny>=0 && ny<N && arr[nx][ny]>h && !ch[nx][ny]) {
                                    q.offer(new Point(nx, ny));
                                    ch[nx][ny] = true;
                                }
                            }
                        }
                    }
                }
                ans = Math.max(ans, temp);
            }
        }
        System.out.println(ans);
    }
}

