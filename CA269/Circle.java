import java.util.*;
import java.awt.*;

public class Circle
{
    private double radius;
    
    public Circle(double r)
    {
        radius = r;
    }
    
    public double getArea() 
    {
        return Math.PI * radius * radius;
    }
    
    public String toString()
    {
        return ("The area is " + String.format("%.3f", getArea()));
    }
}