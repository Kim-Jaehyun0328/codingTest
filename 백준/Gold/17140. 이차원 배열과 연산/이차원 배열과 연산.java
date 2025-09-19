
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int r,c,k;
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken())-1;
        c = Integer.parseInt(st.nextToken())-1;
        k = Integer.parseInt(st.nextToken());
        for(int i=0; i<3; i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(new ArrayList<>());
            for(int j=0; j<3; j++) {
                arr.get(i).add(Integer.parseInt(st.nextToken()));
            }
        }


        process();
        System.out.println(ans);
    }


    static void process() {
        while (true) {
            int row = arr.size();
            int column = arr.get(0).size();

            // 원하는 값이 들어갔으면 종료
            if (row > r && column > c && arr.get(r).get(c) == k) break;
            if (ans > 100) { // 100초 넘어가면 실패
                ans = -1;
                return;
            }

            // 행 연산
            if (row >= column) {
                int newMaxCol = 0;
                ArrayList<ArrayList<Integer>> newArr = new ArrayList<>();

                for (int i = 0; i < row; i++) {
                    HashMap<Integer, Integer> map = new HashMap<>();
                    for (int j = 0; j < column; j++) {
                        int num = arr.get(i).get(j);
                        if (num == 0) continue; // 0은 무시
                        map.put(num, map.getOrDefault(num, 0) + 1);
                    }

                    // map → list 변환 및 정렬
                    ArrayList<int[]> list = new ArrayList<>();
                    for (Map.Entry<Integer, Integer> e : map.entrySet()) {
                        list.add(new int[]{e.getKey(), e.getValue()});
                    }
                    list.sort((a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);

                    // 새로운 행 만들기
                    ArrayList<Integer> newRow = new ArrayList<>();
                    for (int[] p : list) {
                        newRow.add(p[0]);
                        newRow.add(p[1]);
                        if (newRow.size() >= 100) break; // 길이 100 제한
                    }
                    newArr.add(newRow);
                    newMaxCol = Math.max(newMaxCol, newRow.size());
                }

                // 열 길이를 맞추기 위해 0으로 패딩
                for (ArrayList<Integer> rowList : newArr) {
                    while (rowList.size() < newMaxCol) rowList.add(0);
                }

                arr = newArr;

            } else { // 열 연산 (행/열 뒤집어서 처리)
                int newMaxRow = 0;
                ArrayList<ArrayList<Integer>> newArr = new ArrayList<>();

                // 열 단위 데이터를 행처럼 다루기 위해 전치
                for (int j = 0; j < column; j++) {
                    HashMap<Integer, Integer> map = new HashMap<>();
                    for (int i = 0; i < row; i++) {
                        int num = arr.get(i).get(j);
                        if (num == 0) continue;
                        map.put(num, map.getOrDefault(num, 0) + 1);
                    }

                    ArrayList<int[]> list = new ArrayList<>();
                    for (Map.Entry<Integer, Integer> e : map.entrySet()) {
                        list.add(new int[]{e.getKey(), e.getValue()});
                    }
                    list.sort((a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);

                    ArrayList<Integer> newCol = new ArrayList<>();
                    for (int[] p : list) {
                        newCol.add(p[0]);
                        newCol.add(p[1]);
                        if (newCol.size() >= 100) break;
                    }
                    newArr.add(newCol);
                    newMaxRow = Math.max(newMaxRow, newCol.size());
                }

                // 행 길이 맞추기 위해 0 패딩
                for (ArrayList<Integer> colList : newArr) {
                    while (colList.size() < newMaxRow) colList.add(0);
                }

                // 전치해서 다시 저장
                ArrayList<ArrayList<Integer>> transposed = new ArrayList<>();
                for (int i = 0; i < newMaxRow; i++) {
                    ArrayList<Integer> rowList = new ArrayList<>();
                    for (int j = 0; j < newArr.size(); j++) {
                        rowList.add(newArr.get(j).get(i));
                    }
                    transposed.add(rowList);
                }
                arr = transposed;
            }

            ans++;
        }
    }
}
