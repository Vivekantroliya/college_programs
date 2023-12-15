import java.util.Scanner;

interface discount
{
	int discount = 10 ;
	void getData();
	void process();
	void putData();
}

class product implements discount
{
	Scanner p = new Scanner(System.in);

	public void getData()
	{
		System.out.println("Enter Product Name :");
		String pr = p.nextLine();

		System.out.println("Enter Product Price :");
		int pc = p.nextInt();
	}

	public void process()
	{
		float a = (float)pc*discount/100 ;
		float amt = (float)pc - a;
	}

	public void putData()
	{
		System.out.println("Total Amount After Discount :"+amt);
	}
}

class Ex9
{
	public static void main(String[]args)
	{
		product p1 = new product();
		p1.getData();
		p1.process();
		p1.putData();
	}
}