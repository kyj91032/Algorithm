package lambda;

public class LambdaEx1 {

    Object obj = new Object() {
        int max(int a, int b) {
            return a > b ? a : b;
        }
    };

    // max 에 접근을 못함.
}
