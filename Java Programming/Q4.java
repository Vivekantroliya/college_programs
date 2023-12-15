import java.util.Scanner;

class Q4
{
    public static void main(String[]args)
    {
        Scanner rd = new Scanner(System.in);

        System.out.print("Enter Value In Rs. :");
        double rs = rd.nextDouble();

        double dl = rs/82.78;
        System.out.println("Value In Dollars :"+dl);
    }

}