
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static class Point {
        int x, y;
        Point(int a, int b) {
            x=a; y=b;
        }
    }
    static char[][] arr = new char[12][6];
    static Queue<Point> q = new LinkedList<>();

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0; i<12; i++) {
            String str = br.readLine();
            for(int j=0; j<6; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        process();
        System.out.println(ans);
    }

    static void process() {
        while(true) {
            int chk = 0;
            boolean[][] visited = new boolean[12][6];
            for(int i=0; i<12; i++) {
                for(int j=0; j<6; j++) {
                    if(arr[i][j] != '.' && !visited[i][j]) {
                        int cnt = 1;
                        char c = arr[i][j];
                        visited[i][j] = true;
                        ArrayList<Point> list = new ArrayList<>();
                        list.add(new Point(i,j));
                        q.offer(new Point(i,j));
                        while(!q.isEmpty()) {
                            Point p = q.poll();
                            for(int d=0; d<4; d++) {
                                int nx = p.x + dx[d];
                                int ny = p.y + dy[d];
                                if(inRoom(nx, ny) && !visited[nx][ny] && c==arr[nx][ny]) {
                                    visited[nx][ny] = true;
                                    list.add(new Point(nx,ny));
                                    q.offer(new Point(nx, ny));
                                    cnt++;
                                }
                            }
                        }
                        //4개 이상이 모였다면
                        if(cnt>=4) {
                            chk++;
                            for (Point p : list) {
                                arr[p.x][p.y] = '.';
                            }
                        }
                    }
                }
            }
            if(chk==0) break;
            else {
                ans++;
                down();
            }
        }

    }

    static void down() {
        for(int j=0; j<6; j++) {
            for(int i=11; i>=0; i--) {
                if(arr[i][j]!='.') {
                    char c = arr[i][j];
                    int nx = i;
                    while(nx<11 && arr[nx+1][j]=='.') {
                        arr[nx][j] = '.';
                        nx++;
                        arr[nx][j] = c;
                    }
                }
            }
        }


    }

    static boolean inRoom(int x, int y) {
        return (x>=0 && x<12 && y>=0 && y<6);
    }

}
