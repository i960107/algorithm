package stack;


import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Arrays;

public class StockPrice {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Deque<int[]> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int price = prices[i];
            while (!stack.isEmpty() && stack.peekLast()[0] > price) {
                int index = stack.removeLast()[1];
                answer[index] = i - index;
            }
            stack.addLast(new int[]{price, i});
        }
        int maxIndex = stack.removeLast()[1];
        while (!stack.isEmpty()) {
            int currIndex = stack.removeLast()[1];
            answer[currIndex] = maxIndex - currIndex;
        }
        return answer;
    }

    public int[] solution2(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.addLast(0);
        for (int i = 1; i < n; i++) {
            int price = prices[i];
            if (!stack.isEmpty() && price < prices[stack.peekLast()]) {
                int j = stack.pop();
                answer[j] = i - j;
            }
            stack.addLast(i);
        }
        while (!stack.isEmpty()) {
            int j = stack.pop();
            answer[j] = n - 1 - j;
        }

        return answer;
    }

    public static void main(String[] args) {
        StockPrice solution = new StockPrice();
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 2, 3, 2, 3})));
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 2, 3, 4, 5})));
        System.out.println(Arrays.toString(solution.solution(new int[]{5, 4, 3, 2, 1})));
        System.out.println(Arrays.toString(solution.solution(new int[]{4, 3, 2, 5})));
        System.out.println(Arrays.toString(solution.solution(new int[]{1})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{1, 2, 3, 2, 3})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{1, 2, 3, 4, 5})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{5, 4, 3, 2, 1})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{4, 3, 2, 5})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{1})));
    }
}