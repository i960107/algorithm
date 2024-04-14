package stack;

import java.util.*;
import java.util.stream.Collectors;

public class RotateParenthesis {
    private final static Map<Character, Character> parenthesis;

    static {
        parenthesis = new HashMap<>();
        parenthesis.put('}', '{');
        parenthesis.put(']', '[');
        parenthesis.put(')', '(');
    }


    public int solution(String s) {
        int n = s.length();
        String doubledString = s + s;

        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isValid(doubledString, i, i + n)) {
                answer += 1;
            }
        }
        return answer;
    }


    public boolean isValid(String s, int startInclusive, int endExclusive) {
        Deque<Character> deque = new ArrayDeque<>();
        for (int i = startInclusive; i < endExclusive; i++) {
            char c = s.charAt(i);
            if (!parenthesis.containsKey(c)) {
                deque.addLast(c);
            } else if (deque.isEmpty() || !parenthesis.get(c).equals(deque.removeLast())) {
                return false;
            }
        }
        return deque.isEmpty();
    }

    public static void main(String[] args) {
        RotateParenthesis solution = new RotateParenthesis();
        System.out.println(solution.solution("[](){}"));
        System.out.println(solution.solution("}]()[{"));
    }
}