package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * 9046	복호화
 * 피드백 후 정리
 * 1. String 을 순회할 때
 */

public class Main_03 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        for (int i = 0; i < n; i++) {
            Map<Character, Integer> alCount = new HashMap<>();
            String text = bf.readLine().replaceAll("\\s+", "");
            for (char ch : text.toCharArray()) {
                alCount.put(ch, alCount.getOrDefault(ch, 0) + 1);
            }

            int maxCount = -1;
            char maxChar = ' ';
            for (Map.Entry<Character, Integer> entry : alCount.entrySet()) {
                if(entry.getValue() > maxCount) {
                    maxCount = entry.getValue();
                    maxChar = entry.getKey();
                }
            }



        }


    }
}
