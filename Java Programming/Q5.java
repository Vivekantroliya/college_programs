import java.util.Scanner;

class Q5
{
    public static void main(String[]args)
    {
        Scanner r = new Scanner(System.in);
       
        System.out.print("Enter RDBMS Marks :");
        int rdbms = r.nextInt();
        boolean temp=true;
        while(temp){
            if(rdbms>100){
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter RDBMS Marks :");
                rdbms = r.nextInt();
            }
            else if(rdbms<0)
            {
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter RDBMS Marks :");
                rdbms = r.nextInt();
            }
            else
            {
                temp=false;
            }
        }
        temp=true;

        System.out.print("Enter WADUP Marks :");
        int wadup = r.nextInt();
        while(temp){
            if(wadup>100){
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter WADUP Marks :");
                wadup = r.nextInt();
            }
            else if (wadup<0)
            {
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter WADUP Marks :");
                wadup = r.nextInt();
            }
            else
            {
            temp=false;
            }
        }
        temp=true;

        System.out.print("Enter OS Marks :");
        int os = r.nextInt();
        while(temp){
            if(os>100){
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter OS Marks :");
                os = r.nextInt();
            }
            else if(os<0)
            {
                System.out.println("Enter Valid Marks!");
                System.out.print("Enter OS Marks :");
                os = r.nextInt();
            }
            else
            {
                temp=false;
            }
        }
        int total = rdbms+wadup+os;
    
        double per = total/3;

        String result;
        
        if(rdbms>33 && wadup>33 && os>33)
        {
            result = "Pass";
        }
        else
        {
            result = "Fail";
        }

        String className;

        if(per>=90)
        {
            className = "Distinction";
        }
        else if(per>=80)
        {
            className = "First";
        }
        else if(per>=60)
        {
            className = "Second";
        }
        else if(per>=40)
        { 
            className = "Third";
        }
        else if(per>=33)
        {
            className = "Pass";
        }
        else
        {
            className = "Fail";
        }
        
        System.out.println("Total Obtained Marks :"+total);
        System.out.println("Total Obtained Percentage :"+ per +"% ");
        System.out.println("Result :"+result);
        System.out.println("Class :"+className);
    }
}