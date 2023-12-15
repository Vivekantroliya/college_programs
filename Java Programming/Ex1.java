class room
{
    int RollNo;
    String RoomType;
    float RoomArea;
    boolean acMachine;

    void setdata(int a,String b,float c,boolean d)
    {
        RollNo = a;
        RoomType = b;
        RoomArea = c;
        acMachine = d;
    }

    void display()
    {
        System.out.println("My Roll No Is :"+RollNo);
        System.out.println("My Room Type Is :"+RoomType);
        System.out.println("My Room Area Is :"+RoomArea);
        if(acMachine=true)
        {
            System.out.println("Yes,AC Is Needed.");
        }
        else
        {
            System.out.println("No,AC Is Not Needed.");
        }
    }
}

class Ex1
{
    public static void main(String[] args)
    {
    room a = new room();
    a.setdata(1,"2bed bedroom",262.5f,true);
    a.display();
    }
}