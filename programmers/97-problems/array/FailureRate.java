package array;

import java.util.*;

public class FailureRate {
    public int[] solution(int n, int[] arr) {
        int[] challengers = new int[n + 1];
        for (int i = 0; i < arr.length; i++) {
            challengers[arr[i] - 1] += 1;
        }

        int acc = arr.length;
        HashMap<Integer, Double> failRate = new HashMap<>();
        for (int stage = 1; stage <= n; stage++) {
            if (acc == 0) {
                failRate.put(stage, 0.0);
                continue;
            }
            failRate.put(stage, (1.0 * challengers[stage - 1] / acc));
            acc -= challengers[stage - 1];
        }
        System.out.println(failRate);
        //실패율이 높은 순서대로 정렬하는 법이 키뽀인트
        return failRate.entrySet().stream()
                .sorted((o1, o2) ->
                        Double.compare(o2.getValue(), o1.getValue()))
                .mapToInt(HashMap.Entry::getKey)
                .toArray();
    }

    public static void main(String[] args) {
        FailureRate solution = new FailureRate();
        System.out.println(Arrays.toString(solution.solution(5, new int[]{2, 1, 2, 6, 2, 4, 3, 3})));
    }
}