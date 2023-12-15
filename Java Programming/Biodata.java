import java.util.Scanner;

class Biodata{
	public static void main(String[] args){
			
			Scanner myBiodata = new Scanner(System.in);

			System.out.println("Enter Name,Stream,Roll No.,Batch,Mobile No.,Date Of Birth,GR No.,Blood Group,Student Category And Nation :");

			String Name = myBiodata.nextLine();
			String Stream = myBiodata.nextLine();
			String Roll_No = myBiodata.nextLine();
			String batch = myBiodata.nextLine();
			String Mobile_No = myBiodata.nextLine();
			String date = myBiodata.nextLine();
			int GR_No = myBiodata.nextInt();
			String Blood_Group = myBiodata.nextLine();
			String Student_Category = myBiodata.nextLine();
			String Nation = myBiodata.nextLine();

			System.out.println("Name             :"+Name);
			System.out.println("Stream           :"+Stream);
			System.out.println("Roll No.         :"+Roll_No);
			System.out.println("Batch            :"+batch);
			System.out.println("Mobile No.       :"+Mobile_No);
			System.out.println("Date Of Birh     :"+date);
			System.out.println("GR No.           :"+GR_No);
			System.out.println("Blood Group      :"+Blood_Group);
			System.out.println("Student Category :"+Student_Category);
			System.out.println("Nation           :"+Nation);
	}
}