#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int sockMerchant(int n, std::vector<int> ar) {
    std::map<int , int> map;
    for(int val : ar)
    {
        if(map.find(val) == map.end())
        {
            map.insert(std::pair<int, int>(val, 1));
        }
        else {
            map[val] = map[val] + 1;
        }
    }
    int evenCount = 0;
    for(std::pair<int, int> vals : map)
    {
      std::cout << vals.first << ": " <<vals.second << std::endl;
        if(vals.second / 2 > 0)
            evenCount += vals.second / 2;
    }

    return evenCount;
}

int migratoryBirds(std::vector<int> arr) {
    std::map<int , int> map;
    for(int val : arr)
    {
        if(map.find(val) == map.end())
            map.insert(std::pair<int, int> (val, 1));
        else {
        map[val]++;
        }
    }
    for(std::pair<int, int> vals : map)
    {
      std::cout << vals.first << ": " <<vals.second << std::endl;
    }

    return map.begin()->first;
}

bool validTriangle(std::vector<int> lengths)
{
    if(lengths[0] > lengths[1] + lengths[2])
        return false;
    else if(lengths[1] > lengths[0] + lengths[2])
        return false;
    else if(lengths[2] > lengths[1] + lengths[0])
        return false;
    
    return true;
}

std::vector<int> maximumPerimeterTriangle(std::vector<int> sticks) {
    std::vector<int> lengths(3);
    lengths = {sticks[0], sticks[1], sticks[2]};
    
    bool valid = validTriangle(lengths);
    std::vector<int> temp;
    for(int i =3; i < sticks.size() - 1 ; i++)
    {        
        std::sort(lengths.begin(), lengths.end());
        temp.assign(lengths.begin(), lengths.end());
        for(int j =0; j <= 2; j++)
        {
            if(lengths[j] < sticks[i])
            {
                temp[j] = sticks[i];
                valid = validTriangle(temp);
                std::cout << temp[0] <<" "<< temp[1] <<" "<< temp[2] <<" "<<std::endl;
                if(valid)
                    {
                      lengths[j] = sticks[i];
                    }
            }
                
        }    
    }    
    std::reverse(lengths.begin(), lengths.end());
    return valid ? lengths : std::vector<int>(1) = {-1};
}


int main()
{
  std::vector<int> input(5);
  input = {1,1,1,3,3};
  auto ans = maximumPerimeterTriangle(input);
  std::cout << ans[0] <<ans[1] <<ans[2] ;
}
