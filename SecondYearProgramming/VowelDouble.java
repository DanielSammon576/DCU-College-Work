import java.util.Scanner;

public class VowelDouble
{
   public static void main(String [] args)
   {
      System.out.print("Enter a word :");
      String word = new Scanner(System.in).next();
      
      
      word = word.toLowerCase();
      String vowelDouble = "";
      // Insert your code here
      char [] wordList = word.toCharArray();
      String FinalWord = "";
      for(int i = 0; i < wordList.length;i++)
      {
          if(wordList[i] == 'a' || wordList[i] == 'e' || wordList[i] == 'i' || wordList[i] == 'o' || wordList[i] == 'u')
          {
              FinalWord = FinalWord + wordList[i] + wordList[i];
          }
          
          else
          {
              FinalWord = FinalWord + wordList[i];
          }
      }
      
      System.out.println("VowelDoubled is :" + FinalWord + ":");
   }
}
