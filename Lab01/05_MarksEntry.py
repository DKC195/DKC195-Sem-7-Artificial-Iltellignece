n = int(input("Mention the no. of students: "))

name = []
marks = []

for i in range(n):
  name.append(input("Enter Student Name (Roll No. " + str(i+1) + ")"))
  marks.append(input("Enter " + name[i] + "'s Obtained Marks: "))

print("Marks Sheet")
for i in range(n):
  print(name[i] + "\t->\t" + marks[i])
