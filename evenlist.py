def evenlist(start,n):
    a=[]
    for i in range(start,2*n+start):
        if i%2==0:
            a.append(i)
    return a
    
    
    
    
    
print(evenlist(2,4))