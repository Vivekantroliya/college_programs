import java.util.Scanner;

class Q6
{
    public static void main(String[]args)
    {
        Scanner m = new Scanner(System.in);

        System.out.print("Enter First Number :");
        int a = m.nextInt();

        System.out.print("Enter Second Number :");
        int b = m.nextInt();

        if(a>b)
        {
            System.out.println("Largest Value :"+a);
        }
        else
        {
            System.out.println("Largest Value :"+b);
        }
    }

}