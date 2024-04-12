
package array;

import java.util.Arrays;
import java.util.Collections;
import java.util.Set;
import java.util.TreeSet;

public class ControlArray {
    public int[] solution(int[] arr) {
        // TreeSet은 순서가 있다.
        TreeSet<Integer> uniqueValues = new TreeSet<>(Collections.reverseOrder());
        for (int value : arr) {
            uniqueValues.add(value);
        }
        int[] answer = new int[uniqueValues.size()];
        for (int i = 0; i < uniqueValues.size(); i++) {
            answer[i] = uniqueValues.pollFirst();
        }
        return answer;
    }

    public int[] solution2(int[] arr) {
        Integer[] uniqueValues = Arrays.stream(arr).boxed().distinct().toArray(Integer[]::new);
        Arrays.sort(uniqueValues, Collections.reverseOrder());
        return Arrays.stream(uniqueValues).mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        ControlArray solution = new ControlArray();
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 2, 2, 4})));
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 1})));
        System.out.println(Arrays.toString(solution.solution(new int[]{-1, 1})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{1, 2, 2, 4})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{1, 1})));
        System.out.println(Arrays.toString(solution.solution2(new int[]{-1, 1})));
    }
}