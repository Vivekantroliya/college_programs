import java.util.Scanner;

class Sum
{   

    double sum = 0;
    double avg ;
    Sum()
    {
        Scanner input = new Scanner(System.in);

        for(int i=0;i<10;i++)
        {
            System.out.print("Enter Number :");
            double s = input.nextDouble();
            sum += s;
            avg = sum/10;
        }
    
    }

    void display()
    {   
        System.out.println("The Sum Of 10 Numbers :"+sum);
        
        System.out.println("The Average of 10 Numbers :"+avg);
        
    }

}

class Q8
{   
    public static void main(String args[])
    {   
        Sum m =new Sum();
        m.display();
    }
}