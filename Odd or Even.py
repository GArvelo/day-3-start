number = int(input("Which number do you want to check?"))
# % is a modulo operate, which returns the remainder of dividing two numbers.
#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0 :
  print("This is an even number")
#Other (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number")