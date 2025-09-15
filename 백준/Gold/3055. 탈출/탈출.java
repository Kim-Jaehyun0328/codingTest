import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static class Point {
        int x, y, t;
        Point(int a, int b, int c) {
            x=a;
            y=b;
            t=c;
        }
    }

    static int R,C;
    static char[][] arr;
    static boolean[][] sVisited;
    static boolean[][] wVisited;
    static Point S;
    static Queue<Point> sq = new LinkedList<>();
    static ArrayList<Point> W = new ArrayList<>();
    static Queue<Point> wq = new LinkedList<>();

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static boolean flag = false;

    static int ans = Integer.MAX_VALUE;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        arr = new char[R][C];
        wVisited = new boolean[R][C];
        sVisited = new boolean[R][C];
        for(int i=0; i<R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                char c = str.charAt(j);
                arr[i][j] = c;
                if (c == 'S') {
                    S = new Point(i, j, 0);
                    sVisited[i][j] = true;
                    sq.offer(S);
                }
                if (c == '*') {
                    W.add(new Point(i, j, 0));
                    wq.offer(new Point(i, j, 0));
                    wVisited[i][j] = true;
                }
            }
        }

        while(!sq.isEmpty() && !flag) {
            int wSize = wq.size();
            for(int w=0; w<wSize; w++) {
                Point water = wq.poll();
                for(int d=0; d<4; d++) {
                    int nx = water.x + dx[d];
                    int ny = water.y + dy[d];

                    if(nx>=0 && nx<R && ny>= 0 && ny<C && arr[nx][ny] != 'X' && arr[nx][ny] != 'D' && !wVisited[nx][ny]) {
                        wVisited[nx][ny] = true;
                        wq.offer(new Point(nx,ny, water.t+1));
                    }
                }
            }

            int sSize = sq.size();
            for(int s=0; s<sSize; s++) {
                Point temp = sq.poll();
                for(int d=0; d<4; d++) {
                    int nx = temp.x + dx[d];
                    int ny = temp.y + dy[d];
                    //이번 초에 물이 차오르지 않았고 방문한 적이 없는 곳이라면
                    if(nx>=0 && nx<R && ny>= 0 && ny<C && arr[nx][ny] != 'X' && !sVisited[nx][ny] && !wVisited[nx][ny]) {
                        if(arr[nx][ny] == 'D') {
                            flag = true;
                            ans = temp.t+1;
                            break;
                        }
                        sVisited[nx][ny] = true;
                        sq.offer(new Point(nx,ny,temp.t+1));
                    }
                }
            }


        }

        if(flag) System.out.println(ans);
        else System.out.println("KAKTUS");

    }
}
