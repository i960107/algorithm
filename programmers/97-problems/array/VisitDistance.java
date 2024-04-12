package array;

import java.util.HashMap;

public class VisitDistance {
    public int solution(String dirs) {
        HashMap<String, int[]> directions = new HashMap<>();
        // rows, cols
        directions.put("U", new int[]{0, 1});
        directions.put("L", new int[]{0, 1});
        directions.put("D", new int[]{0, 1});
        directions.put("R", new int[]{0, 1});
        return 0;
    }

    public static void main(String[] args) {
        VisitDistance solution = new VisitDistance();
        System.out.println(solution.solution("ULURRDLLU"));
    }
}