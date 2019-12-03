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
        print("\n")
        if(i==2):
            print(i*"___",end="\n")

        for j in range(1, n+1):
            if(j==2):
                print("|",end="  ")

            print("{}".format(i*j),end="  ")





            
x= [1235,5,9,20,234,4,678,547]
def biggest(x):
    big = x[0] 
    for i in x:
        if( i > big ):
            big = i
            
    return big



def biggest2(x):
    big = x[0]
    b = biggest(x)
    if(big == b):
        big=x[1]
    for i in x:
        if( i > big):
            if(i != b):
                big=i

    return [b,big]
                
def biggestn(x):
