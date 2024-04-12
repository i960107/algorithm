package array;


import java.util.Arrays;
import java.util.TreeSet;

public class PickAndAddTwoValue {
    public int[] solution(int[] arr) {
        // 넣을때마다 정렬하느냐 -> 다 넣고 나서 정렬하느냐
        TreeSet<Integer> sumOfTwoValue = new TreeSet<>();
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                sumOfTwoValue.add(arr[i] + arr[j]);
            }
        }
        return sumOfTwoValue.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        PickAndAddTwoValue solution = new PickAndAddTwoValue();
        System.out.println(Arrays.toString(solution.solution(new int[]{2, 1, 3, 4, 1})));
        System.out.println(Arrays.toString(solution.solution(new int[]{5, 0, 2, 7})));
        System.out.println(Arrays.toString(solution.solution(new int[]{1, 1, 1, 1})));
    }
}