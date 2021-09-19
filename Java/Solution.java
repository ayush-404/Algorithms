import javax.swing.event.ChangeEvent;

class Solution {
  public static int threeSumClosest(int[] nums, int target) {
    int[] ans = new int[3];
    for(int change = 0; change < 3; change++)
    {
      ans[change] = nums[change];
    }
    int sum = ans[0] + ans[1] + ans[2];
    int difference = Math.abs(target - sum);
    for(int change = 0; change < 3; change++)
    {
      for(int i = 3; i < nums.length ; i++)
      {
        if(change == 0)
        {
          int new_sum = nums[i] + ans[1] + ans[2];
          if(Math.abs(target -new_sum) < difference)
          {
            difference =  Math.abs(target -new_sum);
            ans[change] = nums[i];
          }
        }
        if(change==1)
        {
          int new_sum = ans[0] + nums[i] + ans[2];
          if(Math.abs(target - new_sum) < difference)
          {
            difference =  Math.abs(target -new_sum);
            ans[change] = nums[i];
          }
        }
        if(change==2)
        {
          int new_sum = ans[0] + ans[1] + nums[i];
          if(Math.abs(target - new_sum) < difference)
          {
            difference =  Math.abs(target -new_sum);
            ans[change] = nums[i];
          }
        }
      }
    }
    return ans[0] + ans[1] + ans[2];
  }

  public static void main(String[] args)
  {
    int[] test = {2,3,4,5,-4,5 , 21};
    System.out.print( threeSumClosest(test, 4));
  }
}