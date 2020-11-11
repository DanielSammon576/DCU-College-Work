import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class MakeMap
{
    // No main method required.
    public static Map makeMap(Scanner in)
    {
        Map<String, Integer> hm = new HashMap< String,Integer>();
        while(in.hasNext())
        {
            String name = in.next();
            int mark = in.nextInt();
            hm.put(name, mark);
        }
        return hm;
    }
}