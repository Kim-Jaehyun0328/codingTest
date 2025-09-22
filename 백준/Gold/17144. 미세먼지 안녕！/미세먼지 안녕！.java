
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R,C,T;
    static int[][] arr;

    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        arr = new int[R][C];
        for(int i=0; i<R; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<C; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[i][j] = num;
            }
        }
        process();
        System.out.println(ans);
    }


    static void process() {
        //T초동안 수행
        for(int t=0; t<T; t++) {
            //먼지 확산
            spread();

            //청소기로 밀어내기
            clean();
        }

        //남아있는 미세먼지 찾기
        findAns();
    }

    static void spread() {
        int[][] temp = new int[R][C];
        for(int i=0; i<R; i++) {
                for(int j=0; j<C; j++) {
                    //미세먼지라면
                    if(arr[i][j] != -1 && arr[i][j] != 0) {
                        int cnt =0;
                        int num = arr[i][j];
                        for(int d=0; d<4; d++) {
                            int nx = i + dx[d];
                            int ny = j + dy[d];
                            //방 안에 있고 진공청소기가 아니면
                            if(inRoom(nx, ny) && arr[nx][ny] != -1) {
                                cnt++;
                                temp[nx][ny] += num/5;
                            }
                            arr[i][j] = num - (num/5) * cnt;
                        }
                    }
                }
            }
        //동시 확산한 거 업데이트
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                arr[i][j] += temp[i][j];
            }
        }
    }

    static void clean() {
        // 공기청정기 위치 찾기
        int top = -1, bottom = -1;
        for (int i=0; i<R; i++) {
            if (arr[i][0] == -1) {
                top = i;
                bottom = i+1;
                break;
            }
        }

        // 1) 위쪽 (반시계)
        // 위 -> 아래로 당김
        for (int i=top-1; i>0; i--) arr[i][0] = arr[i-1][0];
        // 왼 -> 오른쪽 당김
        for (int j=0; j<C-1; j++) arr[0][j] = arr[0][j+1];
        // 아래 -> 위로 당김
        for (int i=0; i<top; i++) arr[i][C-1] = arr[i+1][C-1];
        // 오른 -> 왼쪽 당김
        for (int j=C-1; j>1; j--) arr[top][j] = arr[top][j-1];
        arr[top][1] = 0; // 청정기 옆은 먼지가 사라짐

        // 2) 아래쪽 (시계)
        for (int i=bottom+1; i<R-1; i++) arr[i][0] = arr[i+1][0];
        for (int j=0; j<C-1; j++) arr[R-1][j] = arr[R-1][j+1];
        for (int i=R-1; i>bottom; i--) arr[i][C-1] = arr[i-1][C-1];
        for (int j=C-1; j>1; j--) arr[bottom][j] = arr[bottom][j-1];
        arr[bottom][1] = 0;
    }
    static void findAns(){
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if(arr[i][j] != -1 && arr[i][j] != 0) ans+=arr[i][j];
            }
        }
    }

    static boolean inRoom(int x, int y) {
        return (x>=0 && x<R && y>=0 && y <C);
    }


}
