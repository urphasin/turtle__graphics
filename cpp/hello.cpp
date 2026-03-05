#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;





vector<int> twoSum(vector<int> A, int target) {
  unordered_map<int, int> seen;

  for (int i = 0; i < A.size(); i++) {
    int a = A[i];
    int b = target - a;
    if(seen.find(b) != seen.end()) {
      return {seen[b], i};
    }
    seen[a] = i;
  }
  return {-1};
}

int main() {


  
}