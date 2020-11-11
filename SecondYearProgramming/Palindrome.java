import java.util.*;

public class Palindrome
{
    // Create a static method called makePalindrome with a String parameter which returns a String
    public static String makePalindrome(String word)
    {
        // Your code here
        char [] in = word.toCharArray();
        int begin = 0;
        int end = in.length - 1;
        char temp;
        while (end > begin)
        {
            temp = in[begin];
            in[begin] = in[end];
            in[end] = temp;
            end--;
            begin++;
        }
        return word + new String(in);
    }
}