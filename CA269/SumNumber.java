import java.util.*;
import java.io.*;

public class SumNumber
{
	public static void main(String [] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int n = in.nextInt();
		int sum = 0;
		for(int i = 0; i<=n; i++)
		{
			sum = sum + i;
		}
	System.out.print("The sum of the number from 1 to " + n + " is " + sum);
	}
}