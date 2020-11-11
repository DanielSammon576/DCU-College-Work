//
// Supplied code to help ensure there will be no output formatting issues.
//
import java.util.Scanner;

public class AboveAverage
{
    public static void main(String [] args)
    {
        Scanner in = new Scanner(System.in);
        
        System.out.print("How many numbers: ");
        int num = in.nextInt();
        
        // Create an array
        
        double [] numbers = new double[num];
        
        System.out.print("Enter " + num + " numbers: ");

        // Now read in the numbers
        double sum = 0;
        
        for(int i = 0; i < num; i = i + 1)
        {
            double next = in.nextDouble();
        	numbers[i] = next;
        	sum = sum + next;
        }
        

        double avg = sum / num;
        // Print out the numbers greater than the average
        System.out.println("The above average numbers are:");
        // You can use the following code to print out one number

        for(int i = 0; i < numbers.length; i++)
        {
            if (numbers[i] > avg)
            {
                System.out.print(" " + numbers[i]);
            }
        }

        System.out.println(); // Should finish with a new line
    }
}