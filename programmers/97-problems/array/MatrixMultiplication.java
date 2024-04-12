package array;

import java.util.Arrays;

public class MatrixMultiplication {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int m = arr1.length;
        int n = arr1[0].length;
        int k = arr2.length;

        int[][] answer = new int[m][k];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < k; j++) {
                int result = 0;
                for (int h = 0; h < n; h++) {
                    result += arr1[i][h] * arr2[h][j];
                }
                answer[i][j] = result;
            }
        }
        for (int row = 0; row < answer.length; row++) {
            System.out.println(Arrays.toString(answer[row]));
        }
        return answer;
    }

    public static void main(String[] args) {
        MatrixMultiplication solution = new MatrixMultiplication();
        System.out.println(Arrays.toString(solution.solution(
                new int[][]{{1, 4}, {3, 2}, {4, 1}},
                new int[][]{{3, 3}, {3, 3}})));
        System.out.println(Arrays.toString(solution.solution(
                new int[][]{{2, 3, 2}, {4, 2, 4}, {3, 1, 4}},
                new int[][]{{5, 4, 3}, {2, 4, 1}, {3, 1, 1}})));
    }
}