x = int(input("Enter the obtained percentage: "))

if 100 >= x >= 80:
  print("Distinction")
elif 80 > x >= 65:
  print("First Division")
elif 65 > x >= 55:
  print("Second Division")
elif 55 > x >= 40:
  print("Third Division")
elif 40 > x >= 0:
  print("Fail")
else:
  print("Invalid Percentage")
