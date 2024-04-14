package stack;


import java.util.Stack;

public class ConvertBinaryString {
    public String solution(int decimal) {
        Stack<Integer> stack = new Stack<>();
        while (decimal != 0) {
            stack.push(decimal % 2);
            decimal /= 2;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        ConvertBinaryString solution = new ConvertBinaryString();
        System.out.println(solution.solution(10));
        System.out.println(solution.solution(27));
        System.out.println(solution.solution(12345));
    }
}