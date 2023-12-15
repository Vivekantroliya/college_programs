import java.util.Scanner;

class Pyramid2{

	public static void main(String[] args){
	Scanner p = new Scanner(System.in);
	System.out.print("Enter Number For Pyramid:");
	int n = p.nextInt();

		for(int i=1;i<=n;i++){

			for(int j=i;j>=1;j--)
			{

				System.out.print(j);
			
			}

			System.out.println();
		
		}

	}	

}