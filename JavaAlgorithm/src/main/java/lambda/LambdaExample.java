package lambda;

public class LambdaExample {

    public static void main(String[] args) {



    }

    private static int max(int a, int b) {
        return a > b ? a : b;
    }
    // (a, b) -> a > b ? a : b;

    private static int square(int a) {
        return a * a;
    }
    // a -> a * a;

    private static void printHello() {
        System.out.println("Hello");
    }
    // () -> System.out.println("Hello");

}
