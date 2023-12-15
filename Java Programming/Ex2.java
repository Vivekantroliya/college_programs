class BasicShape
{
    void display()
    {
        System.out.println("Basic Shape");
    }
}

class circle extends BasicShape
{
    void display()
    {   
        super.display();
        System.out.println("This Is Circle.");
    }
}

class polygon extends BasicShape
{
    void display()
    {   
        super.display();
        System.out.println("This Is Polygon.");
    }
}

class ellipse extends BasicShape
{
    void display()
    {   
        super.display();
        System.out.println("This Is Ellipse.");
    }
}

class Ex2
{
    public static void main(String[]args)
    {    
        circle a = new circle();
        a.display();
        polygon b = new polygon();
        b.display();
        ellipse c = new ellipse();
        c.display();
    }
}
