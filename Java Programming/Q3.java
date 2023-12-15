import java.util.Scanner;

class Q3
{
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter Principle Value :");
        double p = in.nextDouble();

        System.out.print("Enter Interest Rate :");
        double r = in.nextDouble();

        System.out.print("Enter Time Duration :");
        double t = in.nextDouble();

        double simple = p*r*t/100;
        System.out.println("Total Simple Interest ="+simple);

        double compound = p*Math.pow((1+r/100),t)-p;
        System.out.println("Total Compound Interest ="+compound);
    }

}