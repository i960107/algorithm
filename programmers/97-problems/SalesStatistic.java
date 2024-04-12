import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SalesStatistic {
    private static String splitor = ",";

    public String[] printSalesStatics(String[] productInfo, String[] dailyProductSales) {
        int n = dailyProductSales.length;
        String[] answer = new String[n];

        Map<String, Product> idProductMap = getIdProductMap(productInfo);


        for (int i = 0; i < n; i++) {
            String[] parsed = dailyProductSales[i].split(splitor);

            String date = parsed[0];
            String id = parsed[1];
            int amount = Integer.parseInt(parsed[2]);
            Product product = idProductMap.get(id);

            String result = concat(date, id, product.getName(), String.valueOf(product.getSalesPrice(amount)));
            answer[i] = result;
        }
        return answer;
    }

    public Map<String, Product> getIdProductMap(String[] productInfo) {
        Map<String, Product> idProductMap = new HashMap<>();
        for (String str : productInfo) {
            String[] parsed = str.split(splitor);
            Product product = new Product(parsed[0], parsed[1], Long.valueOf(parsed[2]));
            idProductMap.put(parsed[0], product);
        }
        return idProductMap;
    }

    public String concat(String... args) {
        StringBuilder sb = new StringBuilder();
        for (String arg : args) {
            sb.append(arg);
            sb.append(splitor);
        }
        sb.delete(sb.length() - 1, sb.length());
        return sb.toString();
    }

    public class Product {
        private String id;
        private String name;
        private Long price;

        public Product(String id, String name, Long price) {
            this.id = id;
            this.name = name;
            this.price = price;
        }

        public String getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public Long getSalesPrice(int amount) {
            return price * amount;
        }

        @Override
        public String toString() {
            return id + name;
        }
    }

    public static void main(String[] args) {
        SalesStatistic salesStatistic = new SalesStatistic();
        String[] result = salesStatistic.printSalesStatics(
                new String[]{"123456789,유기농쌀 4kg,5000", "234578882, 배달이캐릭터숟가락,3000"},
                new String[]{"20220810,123456789,5", "20220810,234578882,30", "20220811,123456789,7"});
        Arrays.stream(result)
                .forEach(x -> System.out.println(x));

    }

}

