n = int(input("Enter a number: ")) 
dup = n
sum = 0 
while n > 0:
    rem = n % 10
    sum = (sum * 10) + rem 
    n = n // 10
if dup == sum:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
