import java.util.HashMap;
import java.util.Map;

class MinimumSubstring
{
  public static String minWindow(String s, String t) {
    Map<Character, Integer> maps = new HashMap<>();
    Map<Character, Integer> mapt = new HashMap<>();
    boolean windowFound = false;
    for(char c : t.toCharArray())
      mapt.put(c, (mapt.get(c) == null? 0: mapt.get(c)) + 1);
    
    for(char c : s.toCharArray())
    {
      mapt.put(c, (mapt.get(c) == null? 0 : mapt.get(c)));
      maps.put(c, (maps.get(c) == null? 0: maps.get(c)) + 1);
    }
      
    int left = 0, right = s.length()-1;

    while(!(right - left < t.length()))
    {
      if(mapt.get(s.charAt(left)) > maps.get(s.charAt(left))
        || mapt.get(s.charAt(right)) > maps.get(s.charAt(right)))
      {
        return "";
      }
      // Check whether apporpriate window is found
      windowFound = true;
      for(char c : mapt.keySet())
      {
        if(maps.get(c) != mapt.get(c))
        {
          windowFound = false;
          break;
        }
      }

      if(windowFound) break;

      if(maps.get(s.charAt(left)) > mapt.get(s.charAt(left)))
      {        
        maps.put(s.charAt(left) , maps.get(s.charAt(left)) - 1);
        left++;
      }
        
      if(maps.get(s.charAt(right)) > mapt.get(s.charAt(right)))
      {        
        maps.put(s.charAt(left) , maps.get(s.charAt(left)) - 1);
        right--;
      }
      System.out.println("Hey");
    }
    return s.substring(left, right);
    
    
  }
  public static void main(String[] args) {
    System.out.println(minWindow("ADOBECODEBANC", "ABC"));
  }
}