def fizzbizz(n):
    for i in range(1, n+1):

        if(i % 15 == 0):
            print("fizzbizz")

        elif(i % 5 == 0):
            print("bizz")

        elif(i % 3 == 0):
            print("fizz")

        else:
            print(i)


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
           # if(abs(i)==abs(j)):
               # if(i==0 or j==0):
               #     print(1,end="  ")
              #  else:
             #       print(abs(i)+1,end="  ")

            elif(abs(i)==k and abs(j)==k):
                print(n,end="  ")

            elif(abs(i)==abs(j)):
                print(abs(i)+1,end="  ")

            else:
                if(abs(i)>abs(j)):
                    print(abs(j)+1,end="  ")

                else:
                    print(abs(i)+1,end="  ")
                   

                

pattern(6)
