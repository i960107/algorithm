import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class CommonElement {
    public String getCommonElement(String[] leftArray, String[] rightArray) {
        Set<String> leftArraySet = new HashSet<String>();
        Set<String> commonElement = new HashSet<String>();
        for (String str : leftArray) {
            leftArraySet.add(str);
        }
        for (String str : rightArray) {
            if (leftArraySet.contains(str)) {
                commonElement.add(str);
            }
        }
        return commonElement.stream().sorted().collect(Collectors.joining(","));
    }

    public static void main(String[] args) {
        CommonElement commonElement = new CommonElement();
        System.out.println(commonElement.getCommonElement(new String[]{"a", "b", "c"}, new String[]{"b", "c", "d"}));
        System.out.println(commonElement.getCommonElement(new String[]{"a", "b", "c"}, new String[]{"c", "b", "a"}));
        System.out.println(commonElement.getCommonElement(new String[]{"a", "b", "c"}, new String[]{"d", "e", "f"}));
        System.out.println(commonElement.getCommonElement(new String[]{"a", "b", "c"}, new String[]{"b", "b", "b"}));
    }
}
