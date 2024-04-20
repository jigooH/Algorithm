package week2;

public class W04 {
    // 논리연산자
    // 비교 연산의 결과값으로 받을 수 있는 boolean 값을 연결하는 연산자
    // 조건을 연결했을 때 boolean 값들을 조합해 참(true) 또는 거짓(false) 값인 boolean 값을 출력
    // &&(and), ||(or), !(not)
    public static void main(String[] args) {
        boolean flag1 = true;
        boolean flag2 = true;
        boolean flag3 = false;

        System.out.println(flag1);
        System.out.println(flag2);
        System.out.println(flag3);

        // 1. 피연산자 중 하나라도 true이면 true : ||(or)
        System.out.println("---------------");
        System.out.println(flag1 || flag2);  // true
        System.out.println(flag1 || flag2 || flag3);  // true
    }
}
