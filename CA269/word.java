import java.util.*;
import java.io.*:

public class word
{
	public static boolean containsLetter(String word, char letter)
	{
		char wordletters [] = word.toCharArray();
		for(int i = 0; i<word.length();i++)
		{
			if(wordletters[i] == letter)
			{
				return true;
			}

			else
			{
				return false;
			}
		}

	}
}