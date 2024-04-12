import java.util.Arrays;
import java.util.HashSet;
import java.util.Locale;

public class MissingCards {
    public long[] missingCards(long[] card) {
        HashSet<Long> set = new HashSet<>();
        for (long c : card) {
            if (set.contains(c)) {
                set.remove(c);
            } else {
                set.add(c);
            }
        }

        return set.stream().sorted().mapToLong(Long::longValue).toArray();
    }

    public static void main(String[] args) {
        MissingCards solution = new MissingCards();
        System.out.println(Arrays.toString(solution.missingCards(new long[]{1, 3, 2, 5, 3, 1})));
        System.out.println(Arrays.toString(solution.missingCards(new long[]{1, 2, 3, 4, 4, 3, 2, 5})));
    }
}
