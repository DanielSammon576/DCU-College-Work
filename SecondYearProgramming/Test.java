import java.util.*;
import java.io.*;

public class Test
{
    public static String [] makeThreesome(String word)
    {
        // Your code here
        String [] letters;
        letters = new String[word.length() - 2];
        for(int i = 2;i<word.length();i++)
        {
        	letters[i-2] == (word.substring(i-2,i + 1));
        }
        return letters;
    }
}