/*
1. 2차원 배열을 하나 생성하고 rectangle 값을 기반으로 값을 채움 (board)
2. 각 꼭지점의 최소 거리를 저장하기 위한 2차원 배열도 생성 (ans)
3. 시작점부터 시작해서 상,하,좌,우 탐색
3-1. 우선 갈 수 있는 지 확인 -> 갈 수 있으면 여기서 상,하,좌,우 탐색 -> 모두 갈 수 있으면 갈 수 없음
3-2. 다음 이동할 좌표에서 대각선 포함 8곳 중 한 곳의 값은 0이어야 함
*/
import java.util.*;
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int r = 102;
        int c = 102;
        int[][] board = new int[r][c];
        int[][] ans = new int[r][c];
        boolean[][] visited = new boolean[r][c];
        int[] dy = new int[]{-1,0,1,0};
        int[] dx = new int[]{0,1,0,-1};
        
        for (int[] rec : rectangle) {
            int x1 = rec[0] * 2;
            int y1 = rec[1] * 2;
            int x2 = rec[2] * 2;
            int y2 = rec[3] * 2;

            for (int i = x1; i <= x2; i++) {
                for (int j = y1; j <= y2; j++) {
                    // 테두리면 1, 내부면 2
                    if (i == x1 || i == x2 || j == y1 || j == y2) {
                        if (board[i][j] != 2) board[i][j] = 1; // 내부 덮지 않기
                    } else {
                        board[i][j] = 2;
                    }
                }
            }
        }
        
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{characterX * 2, characterY * 2, 0});
        visited[characterX * 2][characterY * 2] = true;
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];

            if (x == itemX * 2 && y == itemY * 2) {
                return dist / 2; // 좌표 2배 했으므로 거리도 2배 → 절반 리턴
            }

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx >= 0 && ny >= 0 && nx < 102 && ny < 102 &&
                    !visited[nx][ny] && board[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny, dist + 1});
                }
            }
        }
        
        
        return 0;
    }
}