#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;





vector<int> twoSum(vector<int> A, int target) {
  unordered_map<int, int> seen;

  for (int i = 0; i < A.size(); i++) {
    int b = target - A[i];
    if(b in seen) {
      return {};
    }
    seen[A[i]] = i;
  }
}

int main() {


  
}