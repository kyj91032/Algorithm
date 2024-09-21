package lambda;

@FunctionalInterface // 함수형 인터페이스는 하나의 추상 메서드만 가져야 한다.
public interface MyFunction {
    // 1. 상수
    // 2. 추상 메서드
    // 3. default 메서드

    int A = 100;
    int max(int a, int b);

    default void defaultMethod() {
        System.out.println("default method");
    }
}
