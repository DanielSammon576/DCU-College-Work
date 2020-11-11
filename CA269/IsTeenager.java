import java.util.*;
import java.io.*;

public class IsTeenager
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter your age: ");
		int num = in.nextInt();
		if(num > 12 && num < 20)
		{
			System.out.print("you are a teenager.");
		}
		else
		{
			System.out.print("you are not a teenager.");
		}
	}
}