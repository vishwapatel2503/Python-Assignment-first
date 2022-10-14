# 1.using filter() function filter the list  so that only negative numbers are left.
j=[1,-2,3,-4]
e=list(filter(lambda i:i>0,j))
print(e)



# 2.using filter function filter the even numbers so that only odd numbers are passed to the new list.
i=[1,2,3,4,5,6,7,8,9,10]
j=list(filter(lambda i:i%2!=0,i))
print(j)
k=list(filter(lambda i:i%2==0,i))
print(k)


# 3.using filter() and list() functions and .lower() method filter all the vowels in a given string.

i="Dare to dream then decide to do."
j = list(filter(lambda x: True if x.lower() in "aeiou" else False, i))
print(j)



# 4.This time using filter() and list() functions filter all the positive integers in the string.

i="Vishu eat 5 pani-puri,1 pizza and 1 ice-cream."
j = list(filter(lambda x: True if x in "0123456789" else False, i))
print(j)


#5.Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.
i=[10,-20,30,-40,50,-60,80,-70,-90,100]
j = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, i)))
print(j)


