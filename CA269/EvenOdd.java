import java.util.*;
import java.io.*;

public class EvenOdd
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		List <Integer> odd = new ArrayList<Integer>();
		List <Integer> even = new ArrayList<Integer>();

		System.out.print("Enter numbers:");
		int num = in.nextInt();
		while(num != -1)
		{
			if(num % 2 ==0)
			{
				even.add(num);
			}
			else
			{
				odd.add(num);
			}
			num = in.nextInt();
		}
		String s = "";
		for(int i = 0; i < even.size();i++)
		{
			s+= Integer.toString(even.get(i)) + ", ";
		}
		System.out.println("Even: " + s.substring(0, s.length()-2));
		String t = "";
		for(int i = 0; i < odd.size();i++)
		{
			t += Integer.toString(odd.get(i)) + ", ";
		}
		System.out.println("Odd: " + t.substring(0, t.length()-2));
	}
}