package search;

public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {11, 22, 33, 44, 55, 66, 77};

        int target = 66;

        int left = 0;
        int right = 6;
        int mid = left + right / 2;

        while (left <= right) {
            if (arr[mid] == target) {
                break;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
            mid = (left + right) / 2;
        }

        if (left > right) {
            System.out.println("없음");
        } else {
            System.out.println("해당 인덱스 : " + mid);
        }

    }
}
