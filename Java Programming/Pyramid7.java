import java.util.Scanner;

class Pyramid7{

	public static void main(String[] args){
	Scanner p = new Scanner(System.in);
	System.out.print("Enter Number For Pyramid:");
	int n = p.nextInt();

		for(int i=1;i<=n;i++){

			for(int j=n;j>=i;j--){

				System.out.print(j);
			
			}

			System.out.println();
		
		}
	}	


}