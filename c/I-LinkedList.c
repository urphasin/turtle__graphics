#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node *link;
};

int main() {

  // struct node* newNoode;

  (struct node) *newNode = (struct node*)malloc(sizeof(struct node));
  printf("hello world");
}