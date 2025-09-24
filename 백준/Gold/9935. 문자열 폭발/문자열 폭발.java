
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String boom = br.readLine();
        int boomSize = boom.length();
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<str.length(); i++) {
            stack.push(str.charAt(i));
            //stack size가 boom 문자 길이보다 크거나 같으면 가장 마지막 문자 가져오기
            if (stack.size() >= boomSize) {
                boolean flag = true;
                // boom 문자열 끝에서부터 비교
                for (int j = 0; j < boomSize; j++) {
                    if (stack.get(stack.size() - boomSize + j) != boom.charAt(j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    for (int j = 0; j < boomSize; j++) stack.pop();
                }
            }



        }

        //출력
        if(!stack.isEmpty()) {
            StringBuilder sb = new StringBuilder();
            for (Character c : stack) {
                sb.append(c);
            }
            System.out.println(sb);
        } else System.out.println("FRULA");
    }
}
