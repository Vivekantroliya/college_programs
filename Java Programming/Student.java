class Stud
{
	int id;
	String name;

	public Stud()
	{
		id=1;
		name="test";
	}
	public Stud(int id,String name)
	{
		this.id=id;
		this.name=name;
	}
	public void display()
	{
		System.out.println("My Id Is :"+id);
		System.out.println("My Name Is :"+name);
	}
}
class Student
{
	public static void main(String[] args)
	{
		Stud s1 = new Stud();
		s1.display();
		Stud s2 = new Stud(2,"Vivek");
		s2.display();
	}
}