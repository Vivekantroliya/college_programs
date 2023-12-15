class Animal
{
	Animal()
	{
		System.out.println("Animal Is Created.");
	}
	void sleep()
	{
		System.out.println("Animal Is Sleeping.");
	}
	void eat()
	{
		System.out.println("Animal Is Eating.");
	}
}

class Bird extends Animal
{
	Bird()
	{
		System.out.println("Bird Is Created.");
	}
	void sleep()
	{
		super.sleep();
		System.out.println("Bird Is Sleeping.");
	}
	void eat()
	{	
		super.eat();
		System.out.println("Bird Is Eating.");
	}
}

class Dog extends Animal
{
	Dog()
	{
		System.out.println("Dog Is Created.");
	}
	void sleep()
	{
		System.out.println("Dog Is Sleeping.");
	}
	void eat()
	{
		System.out.println("Dog Is Eating.");
	}
}

class Ex4
{
	public static void main(String[]args)
	{
		Bird b1 = new Bird();
		b1.sleep();
		b1.eat();
		Dog d1 = new Dog();
		d1.sleep();
		d1.eat();
	}
}