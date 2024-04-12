package array;

import java.util.ArrayList;
import java.util.Arrays;

public class MockTest {
    public int[] solution(int[] answers) {
        int[] student1 = {1, 2, 3, 4, 5};
        int[] student2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[][] responses = {student1, student2, student3};

        int[] scores = new int[3];

        for (int i = 0; i < answers.length; i++) {
            int answer = answers[i];
            for (int studentNum = 0; studentNum <= responses.length; studentNum++) {
                int response = responses[studentNum][responses[studentNum].length % i];
                if (response == answer) {
                    scores[studentNum] += 1;
                }
            }
        }
        int maxScore = Arrays.stream(scores).max().getAsInt();
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == maxScore) {
                answer.add(i + 1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        MockTest solution = new MockTest();
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 2, 3, 4, 5})));
    }
}