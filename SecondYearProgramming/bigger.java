import java.util.*;
import java.io.*;

public class bigger
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter two numbers: ");

		int n = in.nextInt();
		int nn = in.nextInt();

		if(n>nn)
		{
			System.out.println(n + " is the biggest number");
		}

		else
		{
			System.out.println(nn + " is the biggest number");
		}
	}
}