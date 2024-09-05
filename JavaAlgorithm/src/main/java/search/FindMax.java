package search;

public class FindMax {
    public static void main(String[] args) {
        int[] arr = {72, 45, 32, 67, 89, 12, 56, 78, 98, 23};

        // stream 사용
        // Arrays.stream(arr).max().ifPresent(System.out::println);

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
}
