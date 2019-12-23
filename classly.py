def digits(n):
    return len(str(n))

def words(s):
    return len(s.split(" "))


def fizzbizz(n):
    if n<=0:
        return 0
    l=[]
    for i in range(1, n+1):

        if(i % 15 == 0):
            print("fizzbizz")
            l.append("fizzbizz")

        elif(i % 5 == 0):
            print("bizz")
            l.append("bizz")

        elif(i % 3 == 0):
            print("fizz")
            l.append("fizz")

        else:
            print(i)
            l.append(i)
    return l


def table2(n):
    for i in range(1, n+1):
        k = []
        print("\n")
        if(i==2):
            print(n*"___",end="\n")

        for j in range(1, n+1):
            if(j==2):
                print("|",end="  ")

            print("{}".format(i*j),end="  ")

#print(table2(5))



            
x= [6,5555,555,9,20,234,4,678,54766]
def biggest(x):
    big = x[0] 
    for i in x:
        if( i > big ):
            big = i
            
    return big



def biggest2(x):
    big2 = x[0]
    big = biggest(x)
    if(big2 == big):
         big2 = x[1]
        
    for i in x:
        if( i > big2):
            if(i < big):
                big2 = i
                
    return [big,big2]


#print(biggest2(x))

def biggestn(x,n):
    l = []
    b = biggest(x)
    l.append(b)
    for i in range(1, n):
        big = x[0]
        for j in range (1, i+1):
            if(big == x[j-1]):
               big = x[j]
        
        
        
        for k in x:
            if( k > big):
                if(k < b):
                    big = k


        b = big
        l.append(b)
    return l

                
def panagram(s):
    s=s.lower()	
    for i in "abcdefghijklmnopqrstuvwxyz":
        if(i not in s):
             return False
    return True
    
#x=panagram("the quick brown fox jumps over the lazy dog")
#print(x)

def freq(s):
    d={}
    for i in s:
        if(i not in d):
            d[ i ] = 1

        else:
            d[ i ] +=1

    return d
#print(freq("fdgsdkgjhnkslnkdfnclbghsfkj;fj;klgheriugzkvcjbvjhjsfdjhfksg"))
            
def pattern(n):
    k=n-1
    l=-k

    for i in range(-k,n):
        print("\n")
        m=k
        for j in range(-k,n):
            if(i==0 or j==0):
                print(1,end="  ")
                print(abs(i)+1,end="  ")
            elif(abs(i)==k and abs(j)==k):
                print(n,end="  ")

            elif(abs(i)==abs(j)):
                print(abs(i)+1,end="  ")

            else:
                if(abs(i)>abs(j)):
                    print(abs(j)+1,end="  ")

                else:
                    print(abs(i)+1,end="  ")
                   

                

#pattern(6)




def denom(n):
    l=[2000,500,200,100,50,20,10,5,2,1]

    for i in l:

        if (n>0):
            k=n//i
            print(f"{k:4} x {i:4} ={i*k:4}")
            print(f"Balance = {n-i*k:4}")
            n-=i*k
                
        
#denoml(55888)

def denomreg(n):

    d={}
    p={}
    l=[2000,500,200,100,50,20,10,5,2,1]
    bal=0

    for i in l:
        print(f"Enter available no of {i}:")
        d[i] = int(input())
        bal += i * d[i]
        #print(bal)

    for i in l:

        k=n//i
        if(n >= bal):
                print("Not enough balance")
                break
        elif (n>0) :
            
            
            if k<=d[i] and k > 0 :
                print(f"{k:4} x {i:4} ={i*k:4}")
                print(f"To pay = {n-i*k:4}")
                
                n -= i*k
                bal -= i*k
                d[i] -= k
                
            elif k > 0:
                if d[i]>0:
                    k = d[i]
                    print(f"{k:4} x {i:4} ={i*k:4}")
                    print(f"To pay = {n-i*k:4}")
                    n -= i*k
                    bal -= i*k
                    d[i] -= k
                
               
    print(f"Available Balance: {bal}")


def atm():

    d={}
    p={}
    l=[2000,500,200,100]
    bal=0

    for i in l:
        print(f"Enter available no of {i}:")
        d[i] = int(input())
        bal += i * d[i]
        

    while True:
        print(f"\n\nAvailable balance:{bal}")
        print(f"\nAvailable denominations \n {d}")
        
        n = int(input("\nEnter amount to withdraw:"))
        amount = n

        for i in l:
            k = n//i
            if(n >=bal):
                print("\n****Not enough balance****")
                break

            

            elif (n>0):

                if k <= d[i] and k > 0:
                    p[i] = k
                    n -= i*k

                elif k>0:
                    if d[i]>0:
                        p[i] = d[i]
                        n -= i*k
                    

        total = 0
        for i in p:
            if i in p:
                total += i*p[i]

        if total == amount:
            print(p)            
            for i in l:
                if i in p:
                    d[i] -= p[i]

            bal=0
        
            for i in l:
                bal += i * d[i]
                if i in p:
                    p[i] = 0

        else:
            print("****NO EXACT DENOMINATION AVAILABLE*****")
            for i in l:
                if i in p:
                    p[i]=0
                    
       # print(d)

        

def postfix(s):
    l=[]
    for i in s:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            l.append(int(i))

        elif i in ['+','-','/','*']:
            a = l.pop()
            b = l.pop()
            if i == '+':
                c = b+a

            elif i == '-':
                c = b-a

            elif i == '*':
                c = b*a
    
            elif i == '/':
                c = b/a

            l.append(c)
    return l.pop()


def in_to_post_fix(s):

    postfix = []
    stack = []
    rank = {'^' : 3 , '*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}

    for i in s:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            postfix.append(i)

        elif i in ['+', '-', '/', '*', '^', '(', ')']:

            if i == ')':

                while True:

                    a = stack.pop()

                    if a == '(':
                        break

                    else:
                        postfix.append(a)
                        
            else:
                if (len(stack)) > 0:
                    b = stack[-1]

                    if rank[i] >= rank[b]:
                        c=stack.pop()
                        postfix.append(c)
                        stack.append(i)

                else:
                    stack.append(i)
                        
    if len(stack)>0:
        l = len(stack)
        for i in range(0,l):
            a = stack.pop()
            postfix.append(a)

    return postfix


def wc():

    filename = input("Enter file name:",)

    txt = open(filename)

    text= txt.read()


    words = len(text.split(" "))-1
    words += len(text.split("\n"))
    if text[-1]=='\n':
        words-=1
    lines = len(text.split("\n"))

    letters = len(text)

    print(f"{words}, {lines}, {letters}  {filename}")
    return words,lines,letters 

    

#wc()
                

                    

                    
            
            
                    
        
