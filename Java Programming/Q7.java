import java.util.Scanner;

class Q7
{
    public static void main(String[]args)
    {
        Scanner m = new Scanner(System.in);

        System.out.print("Enter First Number :");
        int a = m.nextInt();

        System.out.print("Enter Second Number :");
        int b = m.nextInt();

        System.out.print("Enter Third Number :");
        int c = m.nextInt();
        
        if(a == b && b == c && a == c)
        {
            System.out.println("All Values are Equal.");
        }
        else if(a == b)
        {
            System.out.println("Largest Value is First and Second Value :"+a+"&"+b);
        }
        else if(a == c)
        {
            System.out.println("Largest Value is First and Third Value :"+a+"&"+c);
        }
        else if(b == c)
        {
            System.out.println("Largest Value is Second and Third Value :"+b+"&"+c);
        }
        else if(a>=b && a>=c)
        {
            System.out.println("Largest Value is First Value :"+a);
        }
        else if(b>=a && b>=c)
        {
            System.out.println("Largest Value is Second Value :"+b);
        }
        else if(c>=a && c>=b)
        {
            System.out.println("Largest Value is Third Value :"+c);
        }
        
    }

}