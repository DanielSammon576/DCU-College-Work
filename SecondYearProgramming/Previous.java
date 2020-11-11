import java.util.*;
import java.io.*;

public class Previous
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter some numbers (-1 to end)");
		List<Integer> list = new ArrayList <Integer>();
		List<Integer> duplist = new ArrayList <Integer>();

		int num = in.nextInt();
		while(num!=-1)
		{
			if(list.contains(num) == true)
			{
				duplist.add(num);
			}
			else
			{
				list.add(num);
			}
			num = in.nextInt();
		}

		System.out.print("Previous:");
		for(int i=0;i<duplist.size();i++)
		{
			System.out.print(duplist.get(i) + " ");
		}
	}
}