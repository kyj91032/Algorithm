package search;

import java.util.Arrays;

public class FindMax {
    public static void main(String[] args) {
        int[] arr = {72, 45, 32, 67, 89, 12, 56, 78, 98, 23};

        int maximum = findMax(arr);

        System.out.println("최대값 : " + maximum);
    }

    private static int findMax(int[] arr) {
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        return max;
    }

    private static int findMaxByStream(int[] arr) {
        Arrays.stream(arr).max().ifPresent(System.out::println);
    }
}