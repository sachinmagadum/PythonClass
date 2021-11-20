# recursion
# docstring

def sum(n):
    """ recursion function"""
    if n==1:
        return 1
    else:
        return(n+sum(n-1))
    
n=4
z=sum(n)
print(z)
print(sum.__doc__)
# this is programe of finding sum of n number like 1+2+3+n etc, we find sum by
# using of recursion function
# doc string is like comment but this comment is also print in ouput.
# extra == we find out n number of sum by following method of programming.
n=10
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
    print(sum)     # if we print(sum) without 4digit space ans only 55 show.
                    # if we replace while by if then programe show error.
    
# 2nd way
n=10
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)     


    



    



    
      
    
    
    
    

    
    
    
    
    
            
              
    
        


