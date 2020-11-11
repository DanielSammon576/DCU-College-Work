import java.util.*;
import java.io.*;

public class Point implements Order
{
    private double x, y;
    
    public Point(double newX, double newY)
    {
        x = newX;
        y = newY;
    }
    
    public String toString()
    {
        return "(" + x + ", " + y + ")";
    }
    
    public boolean lessThan(Order other)
    {
        Point p = (Point) other;
        if(this.x < p.x)
            return true;
        else if(this.x == p.x)
            if(this.y < p.y)
                return true;
        return false;
    }

}