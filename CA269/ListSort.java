import java.util.*;
import java.io.*;

public class ListSort
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		List<Integer> numbers = new ArrayList<Integer>();
		System.out.print("Enter the numbers: ");

		int num = in.nextInt();
		while(num!=-1)
		{
			numbers.add(num);
			num = in.nextInt();
		}

		Collections.sort(numbers);

		String s = "";
		for(int i = 0; i<numbers.size();i++)
		{
			s += Integer.toString(numbers.get(i)) + " ";
		}

		System.out.print("Sorted: " + s.substring(0, s.length()-1));
	}
}