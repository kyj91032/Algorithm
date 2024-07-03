package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 피드백 후 정리
 * 1. java에서는 input을 받을 때 BufferedReader의 readline
 * 2. String을 순회하는 방법 : for each, stream, for 가 있다.
 *    여기서는 for를 사용했다. for를 사용할 경우 charAt을 사용해 String을 char로 인덱싱한다.
 * 3. char형은 문자의 아스키 값을 갖는다. 정수로 활용할 때는 '0'을 빼준다.
 */

public class Main_00 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String nString = bf.readLine();
        int n = Integer.parseInt(nString);

        String numbers = bf.readLine();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int num = numbers.charAt(i) - '0';
            // char은 아스키 값을 나타냄. 0의 아스키는 48, 1의 아스키는 49... 그래서 '0'(48)을 빼줘야 의도한 값의 정수(1,2,3...)로 쓸 수 있음
            sum += num;
        }
        System.out.println(sum);
    }
}

