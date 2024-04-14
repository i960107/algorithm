package stack;

import java.util.Stack;

public class ClawCrane {
    public int solution(int[][] board, int[] moves) {
        int[] lastRow = getLastRows(board);

        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (int move : moves) {
            Integer popped = pop(board, lastRow, move - 1);
            if (popped == null) {
                continue;
            }
            if (!stack.isEmpty() && stack.peek().equals(popped)) {
                answer += 2;
            } else {
                stack.push(popped);
            }
        }
        return answer;
    }

    public int[] getLastRows(int[][] board) {
        int n = board.length;
        int[] lastRows = new int[n];
        for (int c = 0; c < n; c++) {
            int row = 0;
            while (row + 1 < n && board[row + 1][c] != 0) {
                row += 1;
            }
            lastRows[c] = row;
        }
        return lastRows;
    }

    public Integer pop(int[][] board, int[] lastRows, int col) {
        int row = lastRows[col];
        if (row == -1) {
            return null;
        }

        int result = board[row][col];

        lastRows[col] -= 1;
        board[row][col] = 0;

        return result;
    }

    public static void main(String[] args) {
        ClawCrane solution = new ClawCrane();
        System.out.println(solution.solution(
                new int[][]{{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}},
                new int[]{1, 5, 3, 5, 1, 2, 1, 4}));
    }
public static class FunctionDevelopment {
    public int[] solution(int[] arr) {
    }

    public static void main(String[] args) {
    FunctionDevelopment  solution = new FunctionDevelopment ();
        System.out.println(Arrays.toString(solution.solution(new int[]{})));
    }
}}
