
def mode(s):

    if len(s) == 1:
        return s[0]

    elif len(s) > 1:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1

            else:
                d[i] +=1
        print(d)   
        mode=0
        max=0
        for i in d:
            if d[i] > max:
                mode = i
                max = d[i]
        return mode
        
    else:
        return 0 

mode([1,2,3,4,5,67,84,4,4,4,5,7,8,6,45,4,3,4,4,])
