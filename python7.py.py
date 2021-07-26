def is_even():
    num=int(input("even your number:"))
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')


def is_palindrome():
    st=input("enter string: ")
    if st==st[::-1]:
        print(f'{st} is palindrome: ')
    else:
        print(f'{st} is not a palindrome: ')


def is_prime():
    num=int(input("enter your number: "))
    if num>1:
        for i in range(2,int (num/2)+1):
            if(num%i)==0:
               print(f' {num} is not prime')
               break
        else:
         print(f' {num} is a prime: ')
    else:
         print(f' {num} is not a prime: ')
def is_pos():
    num=int(input("enter your number: "))
    if(num>0):
        print(f' {num} is positive: ')
    else:
        print(f' {num} is negative: ')


def greet_user():
    print("\nhello user\n")
    print('***menu***')
    options=["check odd even\n2.check palindrome\n3.check prime\n4.check positive"]
    for i in range(len(options)):
        print (f'{i+1}.{options[i]}')
    ch=int(input("\nenter your choice:"))
    if ch==1:
       is_even()
    elif ch==2:
        is_palindrome()
    elif ch==3:
        is_prime()
    elif ch==4:
        is_pos()
    else:
        print('\ninvalid choice.\n please try again')
greet_user()             
            
        
