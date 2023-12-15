import java.util.Scanner;

class Q10f
{
    public static void main(String[]args)
    {
        System.out.print("Enter Value For The Series To Be Shown :");
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        int a = 0;
        int b = 1;
        int sum;

        System.out.print("Fibonaci Series :"+a+" "+b+" ");

        for(int i=2;i<n;i++)
        {
            int nextNo = a+b ;
            System.out.print(nextNo+" ");
            a = b;
            b = nextNo;
        }
    }
    
}