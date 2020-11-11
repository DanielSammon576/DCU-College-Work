import java.util.*;
import java.io.*;

public class VowelNumber
{
   public static void main(String [] args)
   {
      System.out.print("Enter a word :");
      String word = new Scanner(System.in).next();
      
      String vowelNumber = "";
      // Insert your code here
      for(int i = 0; i < word.length(); i++)
      {
          if(word.substring(i,i+1).equals("a"))
          {
              vowelNumber = vowelNumber + 1;
          }
          
          if(word.substring(i,i+1).equals("e"))
          {
              vowelNumber = vowelNumber + 2;
          }
          
          if(word.substring(i,i+1).equals("i"))
          {
              vowelNumber = vowelNumber + 3;
          }
          
          if(word.substring(i,i+1).equals("o"))
          {
              vowelNumber = vowelNumber + 4;
          }
          
          if(word.substring(i,i+1).equals("u"))
          {
              vowelNumber = vowelNumber + 5;
          }
          
          else
          {
              vowelNumber = vowelNumber + word.substring(i,i+1);
          }

          vowelNumber = vowelNumber.replaceAll("[AaEeIiOoUu]", "");
      }
      
      System.out.println("VowelNumbered is :" + vowelNumber + ":");
   }
}