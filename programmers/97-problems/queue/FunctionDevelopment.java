package queue;

import java.util.*;
import java.lang.Math;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class FunctionDevelopment {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<int[]> deque = new PriorityQueue<int[]>((o1, o2) -> ((int[]) o1)[0] < ((int[]) o2)[0] ? -1 : 1);
        Math.ceil(100.0 / 33);
        Map<String, Integer> test = new HashMap<>();
        IntStream.range(1, 101).boxed().collect(Collectors.toList());

    }

    public static void main(String[] args) {
        FunctionDevelopment solution = new FunctionDevelopment();
        System.out.println(Arrays.toString(solution.solution(new int[]{93, 30, 55}, new int[]{1, 30, 5})));
    }
}