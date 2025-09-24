
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int N,K;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        String ans = "";
        int cnt = 0;
        String s = br.readLine();
        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        for(int i=1; i<s.length(); i++) {
            char c = s.charAt(i);
            //현재 숫자가 마지막 숫자보다 크다면
            while(!stack.isEmpty() && c>stack.peek() && cnt<K) {
                cnt++;
                stack.pop();
            }
            stack.push(c);
        }
        while(K>cnt) {
            cnt++;
            stack.pop();
        }

        StringBuilder sb = new StringBuilder();
        for (char c : stack) sb.append(c);

        System.out.println(sb);
    }
}
