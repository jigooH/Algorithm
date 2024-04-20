//import java.util.Arrays;
//
//// 클래스
//// publc : 제어자(공공의)
//// 접근을 제어하는 키워드. 퍼블릭의 경우 어디서든 접근 가능
//public class Main {
//
//    // 주석
//
//    // () : 소괄호
//    // {} : 중괄호
//    // [] : 대괄호
//
//    // 소괄호 바로 앞에 있는게 메소드 이름
//    // 현재는 main 메소드
//    // 모든 프로젝트는 main 메소드가 필요. 자바 프로젝트는 제일 먼저 class의 main 메소드를 실행시킨다.
//    // 여기도 퍼블릭이 잇음 : 접근 제어자(외부에서도 접근 가능)
//    // 스태틱 : 이 프로그램이 시작될때 무조건 실행됨을 표현
//    // void : 메서드의 출력값의 데이터타입
//    // void : "아무것도 없다." -> 출력은 없다.
//
//    // input
//    // String[] args : 매개변수 자리
//
//    public static void main(String[] args) {
//
//        // 객체 : 특징(속성, 변수)과 행동(메소드)을 가지고 있음
//        // out이 객체, prinln이라는 메소드를 포함하고 있음
//        // 메소드는 괄호를 열고 닫음으로써 실행 가능, 인풋과 아웃풋을 가지고 있음
//        // 여기서는 "Our First Project! :)"이 인풋
//
//        // print : 줄바꿈x
//        // println : 줄바꿈 o (테스트할때는 보통 println을 씀)
//
//        System.out.println("3");
//        System.out.println(7);
//        System.out.println(3.14);
//        System.out.println("JAVA");
//
//        // 1. boolean
//        // 변수를 선언해보자 -> 타입 이름 = 값;
//        final boolean flag = true;
////        boolean flag;
////        flag = false;
//        System.out.println(flag);
//
//        // 2. 문자형
//        char alphabet = 'A';
//        System.out.println(alphabet);
//
//        // 3. 정수형(byte, short, int, long)
//        byte byteNumber = 127;  // -128~127(1byte)
//        short shortNumber = 32767;  // -32,768~32,767
//        int intNumber = 2147483647;
//        long longNumber = 2147483647;
//
//        System.out.println(byteNumber);
//        System.out.println(shortNumber);
//        System.out.println(intNumber);
//        System.out.println(longNumber);
//
//
//        // 3. 실수형(float, double)
//        float floatNumber = 0.123F;
//        double doubleNumber = 0.123123132;
//
//        System.out.println(floatNumber);
//        System.out.println(doubleNumber);
//
//
//    // 참조형 변수
//        // 1. 문자열 변수
//        String helloworld = "Hello world!";
//        System.out.println(helloworld);
//
//        // 2. 배열
//        int[] a = {1, 2, 3};
//        System.out.println(Arrays.toString(a));
//
//    // 래퍼 클래스(Wrapper Class 변수)
//        int number = 21;
//        Integer num = number;  // boxing
//        System.out.println(num.intValue());  // unboxing
//
//    }
//}

//// 숫자 -> 문자
//import java.util.Scanner;
//
//public class Main {
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        int asciiNumber = sc.nextInt();
//        char ch = (char)asciiNumber; // 문자로 형변환을 해주면 숫자에 맞는 문자로 표현됩니다.
//
//        System.out.println(ch);
//    }
//
//}

// 문자 -> 숫자

//import java.util.Scanner;
//
//public class Main {
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        char letter = sc.nextLine().charAt(0); // 첫번째 글자만 받아오기위해 charAt(0) 메서드를 사용합니다.
//        int asciiNumber = (int)letter; // 숫자로 형변환을 해주면 저장되어있던 아스키 숫자값으로 표현됩니다.
//
//        System.out.println(asciiNumber);
//    }
//
//}

public class Main {

    public static void main(String[] args) {

//        // double or float 형을 int 형으로 바꿔보자
//        // 실수 -> 정수 (0.xxxx -> 0)
//
//        double doubleNumber = 10.101010;
//        float floatNumber = 10.1010f;
//
//        // 변환(int)
//        int intNumber;  // 선언하고
//        intNumber = (int)doubleNumber;  // 변환
//
//        System.out.println("double type -> " + doubleNumber);
//        System.out.println("int type -> " + intNumber);

        // 정수 -> 실수
//        int intNumber = 10;
//        double doubleNumber = (double) intNumber;
//        float floatNumber = (float) intNumber;
//        System.out.println(doubleNumber);
//        System.out.println(floatNumber);

        // 변수 타입별 크기 순서
        // byte(1) -> short(2) -> int(4) -> long(8) -> float(4) -> double(8)
        // 1. byte -> int
        byte byteNumber = 10;
        int intNumber = byteNumber;
        System.out.println(intNumber);

        // char -> int 형변환
        char charAlphabet = 'A';
        intNumber = charAlphabet;
        System.out.println(intNumber);  // A의 유니코드 65

        // int -> long number 형변환
        intNumber = 100;
        long longNumber = intNumber;
        System.out.println(longNumber);

        // int -> double 형변환
        intNumber = 200;
        double doubleNumber = intNumber;
        System.out.println(doubleNumber);



        // 작은 크기의 타입이 큰 크기의 타입과 계산될 때
        // 자동으로 큰 크기의 타이으로 형변환이 일어남
        int Number = 10;
        double doubleNumber1 = 5.5;
        double result = Number + doubleNumber1;
        System.out.println(result);

        // 정수로 나누기
        int iResult = Number / 4;
        // 실수로 나누기
        double dResult = Number / 4.0;

        System.out.println(iResult + " / " + dResult);
    }
}