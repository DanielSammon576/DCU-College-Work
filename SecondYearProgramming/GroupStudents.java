public class GroupStudents
{
   public static void main(String [] args)
   {
      Student [] group = {
               new Student("John", 50),
               new Student("Abby", 40),
               new Student("Dylan", 20),
               new Student("Carl", 70),
               new Student("Maeve", 70),
               new Student("Chris", 46),
               new Student("James", 55),
               new Student("Anne", 63),
            };

      int numPassed = Test.numberPasses(group);
      System.out.println(numPassed + " students passed out of " + group.length);
      System.out.println("That is an " + 100.0 * numPassed / group.length + "% pass rate.");
   }
}