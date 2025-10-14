import java.util.*;

class Solution {
    static boolean[] used;
    static List<String> route = new ArrayList<>();
    static List<String> answerList = new ArrayList<>();
    static boolean found = false;

    public String[] solution(String[][] tickets) {
        used = new boolean[tickets.length];

        // 1️⃣ 티켓을 출발지 기준 → 목적지 기준으로 사전순 정렬
        Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) return a[1].compareTo(b[1]);
            return a[0].compareTo(b[0]);
        });

        // 2️⃣ 시작점 "ICN"으로 DFS 시작
        route.add("ICN");
        DFS("ICN", tickets, 0);

        return answerList.toArray(new String[0]);
    }

    private void DFS(String current, String[][] tickets, int count) {
        // 모든 티켓을 다 썼다면 경로 완성
        if (count == tickets.length) {
            if (!found) { // 첫 번째 완성된 경로가 사전순으로 가장 앞섬
                answerList = new ArrayList<>(route);
                found = true;
            }
            return;
        }

        for (int i = 0; i < tickets.length; i++) {
            if (!used[i] && tickets[i][0].equals(current)) {
                used[i] = true;
                route.add(tickets[i][1]);

                DFS(tickets[i][1], tickets, count + 1);

                // 백트래킹
                used[i] = false;
                route.remove(route.size() - 1);

                // 이미 사전순으로 가장 앞선 경로를 찾았다면 더 탐색할 필요 없음
                if (found) return;
            }
        }
    }
}