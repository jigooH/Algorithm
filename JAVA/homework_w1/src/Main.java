import javax.swing.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
//        1. 입력값
//          - 내가 좋아하는 요리 제목을 먼저 입력
        String title = sc.nextLine();
        title = "[" + title + "]";
//          - 요리 별점을 1~5 사이의 소수점이 있는 실수로 입력 (ex. 3.5)
        float rate = sc.nextFloat();
        sc.nextLine();  // 이 코드 없으면 float 입력받고 남은 개행문자가 input1로 들어가게 됨
//          - 이어서 내가 좋아하는 요리 레시피를 한문장씩 10문장을 입력
        String input1 = sc.nextLine();
        String input2 = sc.nextLine();
        String input3 = sc.nextLine();
        String input4 = sc.nextLine();
        String input5 = sc.nextLine();
        String input6 = sc.nextLine();
        String input7 = sc.nextLine();
        String input8 = sc.nextLine();
        String input9 = sc.nextLine();
        String input10 = sc.nextLine();
//
//        2. 출력값
//          - 입력이 종료되면 요리 제목을 괄호로 감싸서 먼저 출력
        System.out.println(title);
//          - 이어서, 요리 별점을 소수점을 제외한 정수로만 출력 (ex. 3)
        int intRate = (int)rate; // 별점 int형 변환
//          - 바로 뒤에 정수별점을 5점만점 퍼센트로 표현했을때 값을 실수로 출력 (ex. 60.0%)
        double percentageRate = intRate / 5.0 * 100;  // 자동 현변환
//          - 이어서, 입력한 모든 문장앞에 번호를 붙여서 출력
        System.out.println("별점 : " + intRate + " / " + percentageRate);
        System.out.println("1. " + input1);
        System.out.println("2. " + input2);
        System.out.println("3. " + input3);
        System.out.println("4. " + input4);
        System.out.println("5. " + input5);
        System.out.println("6. " + input6);
        System.out.println("7. " + input7);
        System.out.println("8. " + input8);
        System.out.println("9. " + input9);
        System.out.println("10. " + input10);
    }
}