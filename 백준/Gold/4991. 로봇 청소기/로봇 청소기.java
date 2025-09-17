import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int w,h;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    static char[][] arr;
    static int[][] dust;
    static int dustIdx;
    static int[][] dustDist;
    static boolean[][] dustVisited;
    static boolean[] visited;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        while(true) {
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if(w==0 && h==0) break;
            arr = new char[h][w];
            dust = new int[h][w];
            dustIdx = 2;
            for(int i=0; i<h; i++) {
                String str = br.readLine();
                for(int j=0; j<w; j++) {
                    arr[i][j] = str.charAt(j);
                    if(arr[i][j] == 'o') dust[i][j] = 1;
                    if(arr[i][j] == '*') dust[i][j] = dustIdx++;
                }
            }
            dustDist = new int[dustIdx][dustIdx];
            visited = new boolean[dustIdx];
            findDist();
            if(!dustChk(dustIdx)) {
                System.out.println(-1);
                continue;
            }
            ans = Integer.MAX_VALUE;
            cal(1, 1, 0);
            System.out.println(ans);



        }
    }


    static void cal(int cur, int count, int temp) {
        if(count == dustIdx-1) {
            ans = Math.min(ans, temp);
        }
        else {
            for(int i=2; i<dustIdx; i++) {
                if(!visited[i]) {
                    visited[i] = true;
                    cal(i, count+1, temp+dustDist[cur][i]);
                    visited[i] = false;
                }
            }
        }
    }

    static void findDist() {
        Queue<int[]> q = new LinkedList<>();
        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                if(dust[i][j] != 0) {
                    dustVisited = new boolean[h][w];
                    q.offer(new int[]{i,j, 0});
                    dustVisited[i][j] = true;
                    while(!q.isEmpty()) {
                        int[] temp = q.poll();
                        //다른 먼지를 만났을떄
                        if(dust[i][j] != dust[temp[0]][temp[1]] && dust[temp[0]][temp[1]] != '0') {
                            dustDist[dust[i][j]][dust[temp[0]][temp[1]]] = temp[2];
                            dustDist[dust[temp[0]][temp[1]]][dust[i][j]] = temp[2];
                        }

                        for(int d=0; d<4; d++) {
                            int nx = temp[0] + dx[d];
                            int ny = temp[1] + dy[d];
                            if(nx>=0 && nx<h && ny>=0 && ny<w && !dustVisited[nx][ny] && arr[nx][ny] != 'x') {
                                q.offer(new int[]{nx,ny,temp[2]+1});
                                dustVisited[nx][ny] = true;
                            }
                        }
                    }
                }
            }
        }
    }

    static boolean dustChk(int idx) {
        for(int i=2; i<idx; i++) {
            if(dustDist[1][i] == 0) return false;
        }
        return true;
    }
}
