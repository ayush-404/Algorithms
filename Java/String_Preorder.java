import java.util.*;
class String_Preorder
{
  
  public static boolean isValidSerialization(String preorder) {
    String[] nodes = preorder.split(",");
    int balance = 1;
    for(String node : nodes)
    {
      balance--;
      if(balance < 0) return false;
      if(!node.equals("#")) balance+=2;
    }
    return balance == 0;
}
  public static void main(String[] args) {
    String str = "9,#,92,#,#";
    System.out.println(isValidSerialization(str));
  }
}