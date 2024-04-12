package array;

import java.util.Arrays;

public class SortArray {
    public int[] solution(int[] arr) {
        Arrays.sort(arr);
        return arr;
    }

    public static void main(String[] args) {
        SortArray sortArray = new SortArray();
        System.out.println(sortArray.solution(new int[]{1, -5, 2, 4, 3}));
        System.out.println(sortArray.solution(new int[]{2, 1, 1, 3, 2, 5, 4}));
        System.out.println(sortArray.solution(new int[]{6, 1, 7}));

    }
}
