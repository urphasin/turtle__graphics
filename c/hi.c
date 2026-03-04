#include <stdio.h>

typedef int* IntegerPointer;

int main() {

  IntegerPointer A, B;
  *A = 5, *B = 17;

  return 0;
}