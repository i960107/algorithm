package stack;


import java.util.Stack;

public class ValidParenthesis {
    public boolean solution(String str) {
        String LEFT = "(";
        Stack<String> stack = new Stack<>();
        for (String s : str.split("")) {
            if (s.equals(LEFT)) {
                stack.push(LEFT);
            } else if (stack.isEmpty()) {
                return false;
            } else {
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidParenthesis solution = new ValidParenthesis();
        System.out.println(solution.solution("()()"));
        System.out.println(solution.solution("())"));
        System.out.println(solution.solution("(())()"));
        System.out.println(solution.solution("()()(())"));
    }
}