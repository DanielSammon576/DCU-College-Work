import java.util.*;
import java.io.*;

public class Suspicious
{
    public static void main(String [] args)
    {
        try
        {
            Scanner in = new Scanner(System.in);
            //File students = new File("students.txt");
            Scanner students = new Scanner(new File(args[0]));
            Scanner delinquents = new Scanner(new File(args[1]));
            System.out.print(delinquents);
            System.out.print(students);
        }
        catch(FileNotFoundException e)
        {
        }
    }
}