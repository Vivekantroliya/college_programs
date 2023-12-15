import java.util.Scanner;

class max
{
	int a,b,c;
	max()
	{
		Scanner max = new Scanner(System.in);

		System.out.print("Enter First Number :");
		a = max.nextInt();
		System.out.print("Enter Second Number :");
		b = max.nextInt();
		System.out.print("Enter Third Number :");
		c = max.nextInt();	
	}
	void show()
	{
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

class number3
{
	public static void main(String[]args)
	{
		max m=new max();
		m.show();
	}

}