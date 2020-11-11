public class Student
{
    private String name;
    private String ID;
    
    public Student(String a, String iid)
    {
        name = a;
        ID = iid;
    }
    
    public String toString()
    {
        return(name + " " + "(" + ID + ")");
    }
    
    public String getName()
    {
        return name;
    }
    
    public void setName(String sample)
    {
        name = sample;
    }
    
    public String getID()
    {
        return ID;
    }
    
    public void setID(String numbers)
    {
        ID = numbers;
    }
}