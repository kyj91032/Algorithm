package lambda;

public class LambdaEx2 {

    public static void main(String[] args) {

        MyFunction mf = new MyFunction() {

            @Override
            public int max(int a, int b) {
                return a > b ? a : b;
            }
        };

        int result = mf.max(10, 20);
        System.out.println("result = " + result);

        MyFunction mf2 = (int a, int b) -> a > b ? a : b; // 함수형 인터페이스 이기 때문에 함수가 하나뿐임. 람다로 꽂기 가능
        result = mf2.max(11, 22);
        System.out.println("result = " + result);
    }
}
