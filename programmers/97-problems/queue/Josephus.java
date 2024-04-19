package queue;


import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Scanner;

public class Josephus {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        LinkedList<Integer> survivors = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            survivors.addLast(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        int pos = 0;
        while (!survivors.isEmpty()) {
            int index = (pos + k - 1) % survivors.size();
            Integer killed = survivors.remove(index);
            System.out.println(pos + " " +index );
            pos = index;
            if (sb.length() > 1) {
                sb.append(", ");
            }
            sb.append(killed);
        }
        sb.append(">");
        System.out.println(sb);

    }
}
