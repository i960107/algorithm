package stack;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class EditTable {
    private static final int EMPTY = -1;
    private static final int PREV = 0;
    private static final int NXT = 1;

    public String solution(int n, int k, String[] cmd) {
        boolean[] isDeleted = new boolean[n];
        int pos = k;

        int[][] table = new int[n + 2][2];
        for (int i = 1; i < n + 1; i++) {
            table[i][PREV] = i - 1;
            table[i][NXT] = i + 1;
        }

        Deque<Integer[]> deleted = new ArrayDeque();
        for (String s : cmd) {
            System.out.println(pos + Arrays.toString(isDeleted));
            int op = s.charAt(0);
            if (op == 'U') {
                pos = up(table, pos, Integer.parseInt(s.substring(2, 3)));
            } else if (op == 'D') {
                pos = down(table, pos, Integer.parseInt(s.substring(2, 3)));
            } else if (op == 'Z') {
                int undoPos = undo(table, deleted);
                isDeleted[undoPos] = false;
            } else if (op == 'C') {
                isDeleted[pos] = true;
                pos = delete(table, pos, deleted);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(isDeleted[i] ? "X" : "O");
        }
        return sb.toString();
    }

    public int up(int[][] table, int pos, int count) {
        while (pos != EMPTY && count > 0) {
            pos = table[pos][PREV];
            count -= 1;
        }
        return pos;
    }

    public int down(int[][] table, int pos, int count) {
        while (pos != EMPTY && count > 0) {
            pos = table[pos][NXT];
            count -= 1;
        }
        return pos;
    }

    public int delete(int[][] table, int pos, Deque<Integer[]> deleted) {
        int before = table[pos][PREV];
        int nxt = table[pos][NXT]; //마지막이나 첫번째 행을 지우는 경우 주의!;
        if (before != EMPTY) {
            table[before][NXT] = nxt;
        }
        if (nxt != EMPTY) {
            table[nxt][PREV] = before;
        }
        deleted.addLast(new Integer[]{pos, before, nxt});
        return nxt != EMPTY ? nxt : before;
    }

    public int undo(int[][] table, Deque<Integer[]> deleted) {
        Integer[] lastDeleted = deleted.removeLast();
        int before = lastDeleted[1];
        int pos = lastDeleted[0];
        int nxt = lastDeleted[2];
        if (before != EMPTY) {
            table[pos][NXT] = table[before][NXT];
            table[before][NXT] = pos;
        }
        if (nxt != EMPTY) {
            table[pos][PREV] = table[nxt][PREV];
            table[nxt][PREV] = pos;
        }
        return pos;
    }

    public static void main(String[] args) {
        EditTable solution = new EditTable();
        System.out.println(solution.solution(8, 2, new String[]{"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"}));
        System.out.println(solution.solution(8, 2, new String[]{"D 2", "C", "U 3", "C", "D 4", "C", "C", "U 2", "Z", "Z"}));
        System.out.println(solution.solution(8, 2, new String[]{"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"}));
    }
}