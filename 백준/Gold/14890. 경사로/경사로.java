
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N,L;
    static int[][] arr;
    static int ans = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        process();
        System.out.println(ans);
    }



    static void process() {
        //각 행 진행
        for(int i=0; i<N; i++) {
            boolean flag = false;
            flag = crossRow(i);
            //길을 건널 수 있으면 +1
            if(flag) ans++;
        }

        //각 열 진행
        for(int i=0; i<N; i++) {
            boolean flag = false;
            flag = crossColumn(i);
            //길을 건널 수 있으면 +1
            if(flag) ans++;
        }
    }


    static boolean crossRow(int i) {
        int[] line = new int[N];
        boolean[] used = new boolean[N];
        for(int j=0; j<N; j++) {
            line[j] = arr[i][j];
        }

        for(int j=0; j<N-1; j++) {
            int diff = line[j] - line[j+1];
            if(diff == 0) continue;
            // 오르막길
            if (diff == -1) {
                for (int a = j; a > j - L; a--) {
                    if (a < 0 || line[a] != line[j] || used[a]) return false;
                    used[a] = true;
                }
            }
            // 내리막길
            else if (diff == 1) {
                for (int a = j + 1; a <= j + L; a++) {
                    if (a >= N || line[a] != line[j + 1] || used[a]) return false;
                    used[a] = true;
                }
            } else return false;
        }

        return true;
    }


    static boolean crossColumn(int j) {
        int[] line = new int[N];
        boolean[] used = new boolean[N];
        for(int i=0; i<N; i++) {
            line[i] = arr[i][j];
        }

        for(int i=0; i<N-1; i++) {
            int diff = line[i] - line[i+1];
            if(diff == 0) continue;
                // 오르막길
            else if (diff == -1) {
                for (int a = i; a > i - L; a--) {
                    if (a < 0 || line[a] != line[i] || used[a]) return false;
                    used[a] = true;
                }
            }
            // 내리막길
            else if (diff == 1) {
                for (int a = i + 1; a <= i + L; a++) {
                    if (a >= N || line[a] != line[i + 1] || used[a]) return false;
                    used[a] = true;
                }
            } else return false;
        }

        return true;
    }






}
