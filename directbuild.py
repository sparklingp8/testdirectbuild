print("First 100 Fibonnaci numbers are")
a, b = 0, 1
for _ in range(100):
  print(a,", ", sep=", ", end="")
  a, b = b, a+b
