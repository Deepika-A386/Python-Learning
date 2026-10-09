print("Loops")

print("For loop")
n=int(input("Enter a number:"))
for i in range(0,n):
    print(i)

print("Index of sequences")
x=["i","Learn","python"]
for i in range(len(x)):
      print(x[i])

print("While loop")
cnt=0
while (cnt<5):
    cnt=cnt+1
    print(cnt)

print("Nested loops")
for i in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()

