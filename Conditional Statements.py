print("Conditional statements")
print("if statement")
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")

print("if else statement")
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

print("if-elif-else")
age=int(input("Enter your age:"))
if age<=12:
    print("Child")
elif age<=19:
    print("Teenager")
elif age<=35:
    print("Young adult")
else:
    print("Adult")

print("Nested if-else statement")
age=int(input("Enter your age:"))
if age>=12:
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible")
else:
    print("Child")

print("Conditional Expression")
age=int(input("Enter your age:"))
a="Adult" if age>=18 else "Minor"
print(a)

print("Match-Case statement")
number=int(input("Enter a number:"))
match number:
      case 1:
         print("One")
      case 2|3:
         print("Two or Three")
      case _:
         print("Other number")
    
