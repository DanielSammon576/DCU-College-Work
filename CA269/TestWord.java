// Create a Word class with one static method called howManyCorrect
public class TestWord
{
    // Your method here.
    public static int howManyCorrect(String word, String guesses)
    {
        int sum = 0;
        for(int i =0;i<word.length();i++)
        {
            if(containsLetter(guesses, word.charAt(i)))
            {
                sum = sum + 1;
            }
        }
        return sum;

    }
    public static boolean containsLetter(String word, char letter)
    {
        String sample = String.valueOf(letter);
        for(int i = 0; i < word.length(); i++)
        {
            if (sample.equals(word.substring(i,i+1)))
            {
                return true;
            }
        }
        return false;
    }
}