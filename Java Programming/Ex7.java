abstract class person
{
	String name;
	String gender;

	person(String name,String gender)
	{
		this.name = name;
		this.gender = gender;
	}
	abstract void work();
	void display()
	{
		System.out.println("Name :"+name);
		System.out.println("Gender :"+gender);
	}
}

class employee extends person
{
	int empId;

	employee(String name,String gender,int empId)
	{
		super(name,gender) ;		
		this.empId = empId ;
	}
	void work()
	{
		if(empId == 0)
		{
			System.out.println("Employee Is Not Working.");
		}
		else
		{
			System.out.println("Employee Is Working.");
		}
	}
}

class Ex7
{
	public static void main(String[]args)
	{
		employee e1 = new employee("Vivek","Male",0);
		e1.display();
		e1.work();
		employee e2 = new employee("Om","Male",1);
		e2.display();
		e2.work();
	}
}