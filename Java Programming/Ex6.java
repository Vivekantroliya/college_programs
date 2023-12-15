abstract class Instrument
{
	String Name;
	abstract void play();
}

abstract class StringInstrument extends Instrument
{
	int NumberofStrings;
}

class ElectricGuitar extends StringInstrument
{
	ElectricGuitar(String Name,int NumberofStrings)
	{
		super.Name = "Guitar" ;
		super.NumberofStrings = 6 ;
	}
	void play()
	{
		System.out.println("Name Of Instrument :"+Name);
		System.out.println("Number Of Strings  :"+NumberofStrings);
	}
}

class Ex6
{
	public static void main(String[]args)
	{
		ElectricGuitar g1 = new ElectricGuitar("Guitars",7);
		g1.play();
	}
}