import java.util.*;
import java.io.*;

public class SplitWord
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a word: ");
		String word = in.next();

		int i = 1;
		while(i<word.length())
		{
			System.out.print(word.substring(i-1,i+1));
			i++;
		}
	}
}