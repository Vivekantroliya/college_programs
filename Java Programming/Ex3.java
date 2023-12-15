class Info
{
    int pid;
    char branch;
    char year;

    Info(int pid,char branch,char year)
    {
        this.pid = pid;
        this.branch = branch;
        this.year = year;
    }
    public void display()
    {
        System.out.println("Pid :"+pid);
        if(branch == 'i')
        {
            System.out.println("Branch : Information Technology");
        }
        else if(branch == 'e')
        {
            System.out.println("Branch : Electronics and Communication");
        }
        else if(branch == 'c')
        {
            System.out.println("Branch : Computer Science");
        }
        else
        {
        }
        if(year == 'f')
        {
            System.out.println("Year : FE");
        }
        else if(year == 's')
        {
            System.out.println("Year : SE");
        }
        else if(year == 't')
        {
            System.out.println("Year : TE");
        }
        else
        {
        }
        
    }
}

class fe extends Info
{
    int c;
    int cpp;

    fe(int pid,char branch,char year,int c,int cpp)
    {
        super(pid,branch,year);
        this.c=c;
        this.cpp=cpp;
    }
    public void fdisplay()
    {
        super.display();
        System.out.println("C :"+c);
        System.out.println("CPP :"+cpp);
    }
    
}

class se extends Info
{
    int vb;
    int html;

    se(int pid,char branch,char year,int vb,int html)
    {
        super(pid,branch,year);
        this.vb = vb;
        this.html = html;
    }
    public void sdisplay()
    {
        super.display();
        System.out.println("VB :"+vb);
        System.out.println("HTML :"+html);
    }
}

class te extends Info
{
    int java;
    int matlab;

    te(int pid,char branch,char year,int java,int matlab)
    {
        super(pid,branch,year);
        this.java = java;
        this.matlab = matlab;
    }
    public void tdisplay()
    {
        super.display();
        System.out.println("JAVA :"+java);
        System.out.println("MATLAB :"+matlab);
    }
}

class Ex3
{
    public static void main(String[]args)
    {
        fe a = new fe(1,'i','f',99,98);
        a.fdisplay();
        se b = new se(2,'e','s',89,88);
        b.sdisplay();
        te c = new te(3,'c','t',79,78);
        c.tdisplay();
    }
}