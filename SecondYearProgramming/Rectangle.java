public class Rectangle
{
    private double width;
    private double height;
    
    public Rectangle(double w, double h)
    {
        width = w;
        height = h;
    }
    
    public double getArea()
    {
        return width * height;
    }
    
    public String toString()
    {
        return("The area is " + String.format("%.3f", getArea()));
    }
}