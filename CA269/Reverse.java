import java.util.*;
import java.io.*;

public class Reverse
{
	public static int[] reverse(int[] num)
	{
		int[] reverse;
		reverse = new int [num.length];
		int j = num.length - 1;
		for(int i = 0; i < num.length / 2; i++)
		{
			int temp = num[i];
			num[i] = num[j];
			num[j] = temp;
			j--;
		}
		return num;
	}
}