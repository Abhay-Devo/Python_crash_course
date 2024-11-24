# here we will see usage of map, filter, reduce funciton 

from functools import reduce    # for reduce func only rest both doesn't need external lib.


# MAP example:
l = [1, 2, 3, 4, 5]

square = lambda x: x *x

result = map(square, l)   # map func structure = map(function, list)

print(list(result))    # typecasting the output into list
print("")


# FILTER example:
def even(n):
    if(n%2==0):
        return True
    return False

result1 = filter(even, l)
print(list(result1))
print("")


# REDUCE example:
sum = lambda a, b: a+b

result2= reduce(sum, l) 
# reudce will apply the function on the first two values in list, and then will be apply the func on the
# result of first two values and the next value in the list,and go on to end of list.

print(result2)



# another example of reduce is:
g_l= [55, 65, 12, 26, 78, 40, 200, 0, 1]

def greater_num(a, b):
    if(a>b):
        return a
    return b

ans = reduce(greater_num, g_l)
print(f"The Greatest number in the given list is: {ans}")