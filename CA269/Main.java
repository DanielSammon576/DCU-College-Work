import java.util.Scanner;

public class Main
{
    public static void main(String [] args)
    {
        // Create a scanner object
        Scanner in = new Scanner(System.in);
        
        System.out.print("Enter the word: ");
        String word = in.next();

        String [] threes = Test.makeThreesome(word);

        for(String s: threes)
           System.out.println(s);
    }
}