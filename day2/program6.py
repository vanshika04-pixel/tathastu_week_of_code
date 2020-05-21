x=int(input("Enter a number")
temp=x
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//10
if(x==sum):
    printf("number is an armstrong")
else:
    print("not armstorng number")
if(x%2==0):
    print("even number")
else:
    print("odd number")
for i in range(2,x):
    if(x%i)==0:
        print("the number is not a prime number")
        break
else:
    print("number is prime")
rev=0
while(x>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(tem==rev):
    print("the number is palindrome")
else:
    print("number is not palindrome")
