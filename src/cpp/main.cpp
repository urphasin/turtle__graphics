#include <iostream>
#include <vector>
#include <algorithm>








int main() {
  std::vector<int> numbers = {1, 2, 2, 3, 2, 4}  ;

  int result = std::count(numbers.begin(), numbers.end(), 2);

  std::cout << result << "\n";
}