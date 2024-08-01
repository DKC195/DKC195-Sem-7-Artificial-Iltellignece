def ALU(a, b):
  sum = a+b
  differenceA = a-b
  differenceB = b-a
  product = a*b
  quotientA = a/b
  quotientB = b/a
  print("Sum = " + str(sum))
  print("Difference A = " + str(differenceA))
  print("Difference B = " + str(differenceB))
  print("Product = " + str(product))
  print("Quotient A = " + str(quotientA))
  print("Quotient B = " + str(quotientB))

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
ALU(x, y)
