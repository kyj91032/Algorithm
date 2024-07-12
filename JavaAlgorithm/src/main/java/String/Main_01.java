package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 11365	!밀비 급일
 * 피드백 후 정리
 * 1. 자바에서 String 을 역으로 정렬할 때는 StringBuilder를 사용한다.
 *    new StringBuilder(text).reverse().toString();
 */


public class Main_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String line = bf.readLine();
            if (line.equals("END")) {
                break;
            }
            String reversedLine = new StringBuilder(line).reverse().toString();
            System.out.println(reversedLine);
        }
    }
}
