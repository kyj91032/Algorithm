package constructor.model;

import constructor.main.Person;

public class Student extends Person {
    private int grade;

    public Student(String name, int age, int grade) {
        super(name, age);
        this.grade = grade;
    }

    public void printStudentInfo() {
        System.out.println("name : " + name + ", age : " + age + ", grade : " + grade);
    }
}
