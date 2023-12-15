import java.util.Scanner;

class Q1
{
    public static void main(String[] args)
    {
        Scanner Biodata = new Scanner(System.in);

        System.out.print("Enter Name :");
        String Name = Biodata.nextLine();

        System.out.print("Enter Birthdate :");
        String Birthdate = Biodata.nextLine();

        System.out.print("Enter RollNO:");
        long RollNo = Biodata.nextLong();

        System.out.print("Enter GRNO: ");
        long GRNo = Biodata.nextLong();

        Biodata.nextLine();

        System.out.print("Enter Stream :");
        String Stream = Biodata.nextLine();
    
        System.out.println("Name :"+Name);
        System.out.println("Birthdate :"+Birthdate);
        System.out.println("RollNo :"+RollNo);
        System.out.println("GRNo :"+GRNo);
        System.out.println("Stream :"+Stream);
    }

}