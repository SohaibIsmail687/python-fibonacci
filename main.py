#python program for fibonacci series using for loop
n=int(input("Enter the number of terms: "))
a=0
b=1
if n<=0:
    print("The Output of your input is",a)
else:
    print("fibonacci series:")
    print(a)
    print(b)
    for x in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c