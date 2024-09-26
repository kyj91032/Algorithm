package lambda;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class LambdaEx3 {
    public static void main(String[] args) {
        List<String> strList = new ArrayList<>();
        strList.add("a");
        strList.add("b");
        List<String> strList2 = Arrays.asList("a", "b");
        List<Integer> intList = Arrays.asList(5, 1, 2, 3);

        Collections.sort(strList, (o1, o2) -> o1.compareTo(o2));

        for (Integer num : intList) {
            System.out.println(num);
        }
    }
}
