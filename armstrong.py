n = int(input("Enter a number: ")) 
dup = n 
sum = 0  
num_digits = len(str(n)) 
while n > 0:
    rem = n % 10
    sum += rem ** num_digits  
    n //= 10  
if dup == sum:
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")
