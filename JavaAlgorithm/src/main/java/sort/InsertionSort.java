package sort;

public class InsertionSort {

    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 4, 9, 1, 6, 2, 7};
        int temp = 0;
        int j = 0;

        for (int i = 0; i < arr.length - 1; i++) {
            j = i;
            while (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                j--;
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
