import java.util.*;

class collectionEx
{
	public static void main(String[]args)
	{
		ArrayList ar1 = new ArrayList();
		Integer a = new Integer(5);
		Integer b = new Integer(10);
		Integer c = new Integer(15);
		String d = new String("Vivek");

		ar1.add(a);
		ar1.add(b);
		ar1.add(c);
		ar1.add(d);

		System.out.println("The Content Of ArrayList Is :"+ar1);
		System.out.println("The Size Of ArrayList :"+ar1.size());

		ar1.remove(b);
		
		System.out.println("The Content Of ArrayList Is :"+ar1);
		System.out.println("The Size Of ArrayList :"+ar1.size());
	}
}