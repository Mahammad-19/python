n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
n4=int(input("enter fourth number:"))
s=n1
if n2<s:
    s=n2
    if n3<s:
        s=n3
        if n4<s:
            s=n4
            print("the smaller number is:",s)
