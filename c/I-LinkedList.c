#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *link;
} node_t;

int main() {

  node_t* newNoode;

  node_t* newNode = (node_t*)malloc(sizeof(node_t));
  printf("%d\n", newNode->data);
  printf("hello world\n");
}