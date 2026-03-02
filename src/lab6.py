# import turtle

t = "hello"


student = {
    "name": "Otito",
    "age": 18,
    "major": "Math"
}
print(student.get("names"))






def print_address(**something):
  for values in something.values():
    print(values, end=", ")
  print()
print_address(
  street= "1375 Village Loop Rd",
  city= "Ogden",
  zipcode= "84403",
  state="Utah"
)



navlist = ["banana", "mangos", 45768, "pinefruit"]
print(navlist.index("mangos"))
print(navlist.index(45768))
print("hello world")
# print(help(list))
print("\n\n")
# print(dir(my_list))


friends = {
  "brady": 2,
  "desmond": 4,
  "krishna": 4
}

family = {
  "mom": 156,
  "amarachi": 2, 
  "ebube": 4,
  "otito": 356749036, 
}

print(family.setdefault("mom", 999))

print(family.get("otito"))

print(family.setdefault("name", "Luigi"))

print(family.get("name"))


courses = {
  "cs1300": "hard",
  "cs1400": "hard",
  "web1400": "hard",
  "math1050": "hard",
  "math1060": "hard"
}


words = ["apple", "banana", "apricot", "blueberry"]

groups = {}






class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # list of GraphNode

    def add_edge(self, node):
        self.neighbors.append(node)
a = GraphNode("A")
b = GraphNode("B")
c = GraphNode("C")
a.add_edge(b)
a.add_edge(c)        




class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
a = SinglyNode(1)
b = SinglyNode(2)
c = SinglyNode(3)
a.next = b
b.next = c        




class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
a = DoublyNode(1)
b = DoublyNode(2)
a.next = b
b.prev = a




class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)