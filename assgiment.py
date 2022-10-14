#1 = Triple all the numbers given in list:
num=map(lambda i:i+i+i,[1,2,3])
print(list(num))


#2 = Separate even odd number from given list:
j=[1,2,3,4]
even=[]
odd=[]
for i in j:
    if(i%2==0):
        even.append(i)
        
    else:
        odd.append(i)
    
print("Even List:",even)
print("Odd List:",odd)



#3 = Print all string in lower case from given tuple:
def lower (str):
    return str.lower()
str=map(lower,("HI","GOOD MORNING"))
print(tuple(str))


#4 = Print square root of numbers given in list:
def root(i):
    #p=power
    p=0.5
    return i**p
i=map (root,[4,9,16])
print(list(i))


#5 = Eliminate duplicate letter from given string:
def removeduplicate(i, n):
    s = set()
    for i in i:
        s.add(i)
    ss =""
    for i in s:
        ss = ss+i
    return ss
i = "Vishwa Patel"
n = len(i)
print(removeduplicate(list(i), n))



#6 = Print table of any number:
j = int(input("Enter the number: "))
for i in range (1, 11):
    print(j, "x", i, "=", j * i)
    
  
#7 = Add two list:
i=[1,2,3]
j=[4,5,6]
print(list(i+j))

#8 = Convert all float digits into integer using built in function from given list:
i=1.5
print(int(i))

#9 = Reverse given set:
s = ('A', 'B', 'C', 'D', 'E')
print(list(reversed(s)))

#10 = Add '@gmail.com' to all the values 
#of given dictionary and convert it to lower case:

dict_item={"A":"AA","B":"BB","C":"CC"}
a=map(lambda i:(i[0],i[1]+"@gmail.com"),dict_item.items())
print(dict(a))



   
