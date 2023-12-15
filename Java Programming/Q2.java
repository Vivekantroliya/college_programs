import java.util.Scanner;

class Q2
{
    public static void main(String[]args)
    {
        Scanner Math = new Scanner(System.in);

        System.out.print("Enter Number A:");
        int A = Math.nextInt();

        System.out.print("Enter Number B:");
        int B = Math.nextInt();

        int sum = A+B;
        System.out.println("Summation :"+sum);

        int sub = A-B;
        System.out.println("Substraction :"+sub);

        int multi = A*B;
        System.out.println("Multiplication :"+multi);

        double div = (double)A/(double)B;
        System.out.println("Division :"+div);

        int mod =A%B;
        System.out.println("Modulo :"+mod);
    }
}