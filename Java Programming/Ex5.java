abstract class Vehicle
{
	abstract void engine();
}

abstract class Car extends Vehicle
{
	abstract void engine();
}

class BMW extends Car
{
	void engine()
	{
		System.out.println("BMW Car Engine.");
	}
}

class Ex5
{	
	public static void main(String[]args)
	{
		BMW c1 = new BMW();
		c1.engine();
	}
}