freq = {}
arr = [4, 4, 4, 2, -1, 1, 2, 0, 3, 2]

max_val = float('-inf')
min_val = float('inf')

for x in arr:
  if x >= max_val:
    max_val = x

  if 0 < x <= min_val:
    min_val = x


print("max val :", max_val)
print("min val :", min_val)
print("")


for x in arr:
  freq[x] = freq.get(x, 0) + 1

print("Pos : Value")
for pos, val in freq.items():
  print(pos,":", val)