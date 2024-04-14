package stack;

import java.util.Deque;
import java.util.ArrayDeque;

public class PairRemove {
    public int solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (stack.isEmpty() || !stack.peekLast().equals(c)) {
                stack.addLast(c);
            } else {
                stack.removeLast();
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        PairRemove solution = new PairRemove();
        System.out.println(solution.solution("baabaa"));
        System.out.println(solution.solution("cdcd"));
        System.out.println(solution.solution("cd"));
        System.out.println(solution.solution("ccdd"));
    }
}