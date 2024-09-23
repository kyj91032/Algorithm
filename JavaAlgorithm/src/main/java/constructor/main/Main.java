package constructor.main;

import constructor.model.Person;

public class Main {
    public static void main(String[] args) {
        Person p1 = new Person("이름입니다", 25);

        System.out.println("p2.age : " + p1.age);
        System.out.println("p2.name : " + p1.name);
    }
}
