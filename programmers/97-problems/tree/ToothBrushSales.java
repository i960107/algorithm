package tree;

import java.util.HashMap;
import java.util.Map;

public class ToothBrushSales {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int n = enroll.length;
        Map<String, Integer> people = new HashMap<>();
        for (int i = 0; i < n; i++) {
            people.put(enroll[i], i);
        }

        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            if (!referral[i].equals("-")) {
                parent[i] = people.get(referral[i]);
            } else {
                parent[i] = -1;
            }
        }


        int[] sales = new int[n];
        for (int i = 0; i < seller.length; i++) {
            distributeProfit(sales, parent, people.get(seller[i]), amount[i] * 100);
        }
        return sales;
    }

    public void distributeProfit(int[] sales, int[] parent, int sellerId, int price) {
        while (sellerId != -1) {
            int others = (int) (price * 0.1);
            int distributed = price - others;
            //int distributed = (int)(price * 0.1) == 0? price: (int)(price * 0.9);
            sales[sellerId] += distributed;
            price -= distributed;
            sellerId = parent[sellerId];
        }
    }
}
}
