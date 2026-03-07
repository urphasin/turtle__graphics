#include <stdio.h>
#include <stdlib.h>

typedef int*  IntegerPointer;
typedef int   Integer;



int main() {

  Integer         Y = 5,  Z = 17; 
  IntegerPointer  A = &Y, B = &Z;

  *A = 5, 
  *B = 17;

  int* a = malloc(sizeof(int));
  *a = 6;

  printf("%d : \n", *a);

  // free(a);
  // free(A);
  // free(B);

  return 0;
}