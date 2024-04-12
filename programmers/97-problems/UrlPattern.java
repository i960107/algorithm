import java.util.Arrays;
import java.util.regex.Pattern;

public class UrlPattern {
    private static final String ERROR = "error";
    private static final String URL_REGEX = "^/payment/\\d{1,9}/[a-zA-Z]{1,10}$";
    private static final String SPLITOR = "/";
    private static final String START_QUERY_PARAMETER = "?";
    private static final String PREFIX = "/payment/";

    public String urlPattern(String url) {
        if (!isValidUrl(url)) {
            return ERROR;
        }

        String[] parsed = url.split(SPLITOR);
        String pathVariable = parsed[2];
        String paymentMethod = parsed[3];

        StringBuilder sb = new StringBuilder();
        sb.append(PREFIX);
        sb.append(paymentMethod);
        sb.append(START_QUERY_PARAMETER);
        sb.append("paymentId=");
        sb.append(pathVariable);
        return sb.toString();
    }

    public boolean isValidUrl(String url) {
        return url.matches(URL_REGEX);
    }

    public static void main(String[] args) {
        UrlPattern solution = new UrlPattern();
        System.out.println(solution.urlPattern("/payment/1234/cancel"));
        System.out.println(solution.urlPattern("/payment/1234"));
        System.out.println(solution.urlPattern("/payment/a1234/cancel"));
        System.out.println(solution.urlPattern("/pyment/1234/cancel"));
        System.out.println(solution.urlPattern("/payment/123412341234/cancel"));
        System.out.println(solution.urlPattern("payment/123/cancel"));
        System.out.println(solution.urlPattern("/payment/123/567"));
        System.out.println(solution.urlPattern("/payment/123/cancel/"));
    }
}
