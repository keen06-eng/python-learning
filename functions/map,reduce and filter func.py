from functools import reduce
#Map() function and lambda function
sqr= lambda x:x**2
a=[1,2,3,4]
res=list(map(sqr,a))
print(res)
#using multiple iterables
b=[1,2,3]
c=[4,5,6]
itr=list(map(lambda x,y:x+y,b,c))
print(itr)


#reduce() function
s=[2,3,4,5]
rez=reduce(lambda x,y:x+y,s)
print(rez)

#filter() function
n=[1,-2,4,0,7]
rezz=filter(lambda x:x>5,n)
print(list(rezz))