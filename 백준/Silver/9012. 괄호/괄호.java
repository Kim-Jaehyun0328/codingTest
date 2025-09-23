
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for(int i=0; i<T; i++) {
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();
            boolean flag = true;
            for(int j=0; j<str.length(); j++) {
                char c = str.charAt(j);
                if(c =='(') stack.push(c);
                else {
                    if(stack.isEmpty()) {
                        flag = false;
                        break;
                    }
                    stack.pop();
                }
            }
            if(flag && stack.isEmpty()) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
