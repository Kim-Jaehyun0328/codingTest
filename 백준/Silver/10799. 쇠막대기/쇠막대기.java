
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        Stack<Character> stack = new Stack<>();
        int ans = 0;
        boolean flag = false;
        char last = 'a';
        for(int i=0; i<str.length(); i++) {
            char c = str.charAt(i);
            if(c=='(') {
                stack.push(c);
            } else if(c==')') {
                //레이저
                if(last == '(') {
                    stack.pop();
                    ans += stack.size();
                } else {
                    stack.pop();
                    ans+=1;
                }
            }
            last = c;
        }

        System.out.println(ans);
    }
}
