interface Printable
{
	void print();
}

interface Showable
{
	void show();
}

class InterfaceEx implements Printable,Showable
{
	public void print()
	{
		System.out.println("Hello");
	}
	public void show()
	{
		System.out.println("Welcome");
	}
}

class Ex8
{
	public static void main(String[]args)
	{
		InterfaceEx i1 = new InterfaceEx();
		i1.print();
		i1.show();
	}
}