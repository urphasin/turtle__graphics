#define MAXSTACKSIZE 100

typedef char ItemType;

typedef struct {
          int       Count;
          ItemType  Items[MAXSTACKSIZE];
} Stack;