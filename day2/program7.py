n=int(input("enter number of terms for the fibonnaci series:"))
n1=0
n2=1
count=0
if(n<=0):
    print("please enter positive numer of terms")
elif n==1:
    print("Fibonnaci series is ",n1)
else:
    print("Fibonnaci series:")
    while(count<n):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
    
