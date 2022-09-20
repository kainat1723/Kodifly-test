# Find the sum of the digits in the number 100!
# Defining required functions
#Part1 Factorial of a number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
#Part2 Sum of the digits
def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

num = 100; #Required input
new_num = factorial(num); 
Q1 = getSum(new_num);
print("Factorial of",num,"is",new_num);
print ("Answer of Q1 is: ", Q1);