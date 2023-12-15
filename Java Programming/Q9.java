import java.util.Scanner;

class Q9
{
    public static void main(String[]args)
    {
        Scanner s = new Scanner(System.in);

        double max = Double.MIN_VALUE;

        for(int i=0;i<10;i++)
        {
            System.out.print("Enter Number :");
            double num = s.nextDouble();
            if(num>max)
            {
                max = num;
            }
        }
        System.out.println("The Maximum Number Is "+max);
    }
}