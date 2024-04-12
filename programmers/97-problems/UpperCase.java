import java.util.Arrays;
import java.util.Optional;

public class UpperCase {
    public String upperCase(String[] input) {
        Optional<String> result = Arrays.stream(input)
                .filter(str -> str.length() >= 5 && str.length() <= 10)
                .map(String::toUpperCase)
                .findFirst();
        return result.orElse("없음");
    }

    public static void main(String[] args) {
        UpperCase solution = new UpperCase();
        System.out.println(solution.upperCase(new String[]{"sa", "serialize", "012", "없음"}));
    }
}
