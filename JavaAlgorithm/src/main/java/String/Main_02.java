package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 3029	경고
 * 피드백 후 정리
 * 1. 문자열을 문자 기준으로 나눌 때는 .split() 메소드를 사용한다.
 * 2. 문자열을 포멧팅하여 출력할 때는 .format() 메소드를 사용한다.
 *    ex) "%02d" 라면 두자리보다 작으면 0으로 채워 정수를 출력
 */

public class Main_02 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] now = bf.readLine().split(":");
        String[] target = bf.readLine().split(":");

        StringBuilder sb = new StringBuilder();

        int h = Integer.parseInt(target[0]) - Integer.parseInt(now[0]);
        int m = Integer.parseInt(target[1]) - Integer.parseInt(now[1]);
        int s = Integer.parseInt(target[2]) - Integer.parseInt(now[2]);

        if(s < 0) {
            s += 60;
            m--;
        }

        if(m < 0) {
            m += 60;
            h--;
        }

        if(h < 0) {
            h += 24;
        }

        if (Arrays.equals(now, target)) {
            sb.append("24:00:00");
        } else {
            sb.append(String.format("%02d:%02d:%02d", h, m, s));
        }

        System.out.println(sb);
    }
}
