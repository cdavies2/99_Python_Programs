# Let's do the 99 prolog problems

# 1. Find the last element of a list
myList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList[-1])

# 2. Find the last but one element of a list
print(myList[-2])

# 3. Find the Kth element of a list
whichOne=int(input("Which element of the list do you want? "))
while whichOne>9:
    whichOne=int(input("Out of range, please try again "))

print("The element is", myList[whichOne-1]) #indexes of a list start at 0, so subtract 1

# 4. Find the number of elements of a list
print(len(myList))
# 5. Reverse a list
reverseList=list(reversed(myList))
print(reverseList)
# 6. Find out whether a list is a palindrome
testList=['r', 'a', 'c', 'e', 'c', 'a', 'r']
reverseTest=list(reversed(testList))

if (myList == reverseList):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

#make sure it works with both
if (testList == reverseTest):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
# 7. Flatten a nested list structure
flattenThis=['a', 'b', ['c', 'd'], 'e']

for i in flattenThis:
    if type(i)==list:
        for j in i:
            flattenThis.insert(flattenThis.index(i), j)
        flattenThis.remove(i)

print(flattenThis)

# 8. Eliminate consecutive duplicates of list elements

compressIt=['a','a','a','b', 'c','c','c','d','e','e']
compressed=[]
for j in compressIt:
    if j not in compressed:
        compressed.append(j)

compressIt=compressed
        
    
print(compressIt)


# 9. Pack consecutive duplicates of list elements into sublists
compressIt=['a','a','a','b', 'c','c','c','d','e','e']

def pack(l):
    packedList=[]
    finalList=[]
    for i in l:
        packedList.append(i)
        countIt=l.count(i)
        for j in range(countIt-1):
            packedList.append(i)
            l.remove(i)
        finalList.append(packedList)
        packedList=[]
        
    return finalList


print(pack(compressIt))
    

# 10. Run-length encoding of a list
compressIt2=['a','a','a','b', 'c','c','c','d','e','e']
def run_length(l):
    placeList=[]
    finalList=[]
    for i in l:
            num=l.count(i)
            placeList.append(i)
            placeList.append(num)
            finalList.append(placeList)
            for j in range(num-1):
                l.remove(i)
            placeList=[] 
    return finalList
print(run_length(compressIt2))
# 11. Modified run-length encoding
compressIt3=['a','a','a','b', 'c','c','c','d','e','e']
def run_length_mod(l):
    placeList=[]
    finalList=[]
    for i in l:
            num=l.count(i)
            if num>1:
                placeList.append(i)
                placeList.append(num)
                finalList.append(placeList)
            else:
                finalList.append(i)
            for j in range(num-1):
                l.remove(i)
            placeList=[] 
    return finalList
print(run_length_mod(compressIt3))

# 12. Decode a run-length encoded list

# 13. Run-length encoding of a list (direct solution)


# 14. Duplicate the elements of a list
duplicateIt=['r', 'a', 't', 's']
dummyList=[]
for i in duplicateIt:
    if i not in dummyList:
        duplicateIt.insert(duplicateIt.index(i), i)
        dummyList.append(i)

print(duplicateIt)

# 15. Duplicate the elements of a list a given number of times
multiList=['d', 'o', 'g', 's']
def multiply(l, m):
    if type(l)!=list:
        return "Invalid input"
    placeholder=[]
    for i in l:
        if i not in placeholder:
            placeholder.append(i)
            for j in range(m):
                l.insert(l.index(i), i)
    return l

print(multiply(multiList, 3)) #the second value is the number of times you're duplicating each element

# 16. Drop every nth element from a list

dropList=['p', 'y', 't', 'h', 'o', 'n']
def dropEvery(l, d):
    if type(l)!=list:
        return "Invalid input"
    count=0
    for i in l:
            count+=1
            if count%d==0:
                del l[l.index(i)]
                count+=1 #accounts for how the position of count may change after an item is deleted
        
    return l

print(dropEvery(dropList, 2))

# 17. Split a list into two parts: the length of the first part is given
l1=['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']


def split(l, g):
    newList=[]
    newList2=[]
    count=0
    for i in l:
        count+=1
        if count<=g:
            newList.append(i)
        else:
            newList2.append(i)
    return newList, newList2
print(split(l1, 5))

# 18. Extract a slice from a list

def sliceIt(l1, I, K):
    return l1[I-1:K]

print(sliceIt(l1, 4, 7))
    
# 19. Rotate a list N places to the left
l2=[1, 2, 3, 4, 5, 6, 7, 8]

# 20. Remove the Kth element from a list
l3=['M', 'A', 'T', 'H']
def remove_at(l, p):
    del l[p-1]
    return l
print(remove_at(l3, 2))

# 21. Insert an element at a given position into a list
def insert_at(l, e, p):
    l.insert(e-1, p)
    return l

print(insert_at(l3, 2, 'O'))

# 22. Create a list containing all integers within a given range
def all_ints(sr, er):
    newL=[]
    for i in range(sr, er+1):
        newL.append(i)
    return newL
print(all_ints(4, 9))


# 23. Extract a given number of randomly selected elements from a list
l4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random
def random_select(l, n):
    newList=[]
    for i in range(n):
        ran=random.randrange(0, len(l)-1)
        newList.append(l[ran])
        del l[ran]
    return newList

print(random_select(l4, 3))

# 24. Lotto: Draw N different random numbers from the set 1..M
def lotto(n):
    l=all_ints(1, 49)
    ticket=random_select(l, n)
    return ticket

print(lotto(6))

# 25. Generate a random permutation of the elements of a list
def rnd_permu(l):
    newList=[]
    for i in l:
        ran=random.randrange(0, len(l)-1)
        move_to=l[ran]
        newList.insert(move_to, i)
    return newList

print(rnd_permu(l4))



#Let's do some arithmetic ones

# 31. Determine whether a given integer number is prime
def is_prime(num):
    count=0
    for i in range(2, num-1):
        if num % i == 0:
            count+=1
    if count >=1:
        return "This number isn't prime"
    else:
        return "This number is prime"
print(is_prime(5))
print(is_prime(9))

# 32. Determine the greatest common divisor of two positive integer numbers
def euclid(f1, f2):
    while((f1%f2)!=0):
        quotient=f1%f2
        f1=f2
        f2=quotient
    return f2

print(euclid(27, 12))

# 33. Determine whether two positive integer numbers are coprime
def is_coprime(n1, n2):
    while((n1%n2)!=0):
        q=n1%n2
        n1=n2
        n2=q
    if n2==1:
        return "Yes"
    else:
        return "No"
print(is_coprime(10, 3))
print(is_coprime(10, 4))

# 34. Calculate Euler's Totient Function phi(m)
def totient(n):
    tally=1
    if n==1:
        tally=1
    for i in range(1, n):
        if (is_coprime(n, i)=='Yes'):
            tally+=1
    return tally

print(totient(4))
print(totient(7))

# 35. Determine the prime factors of a given positive integer
def prime_f(num):
    p_factors=[]
    p_list=[]
    for i in range(2, num+1):
        if is_prime(i)=='This number is prime':
            p_list.append(i)
    if len(p_list)==1:
        p_factors.append(p_list[0])
    else:
        while(num>1):
            for i in p_list:
                if num%i==0:
                    p_factors.append(i)
                    num=num/i
    return p_factors

print(prime_f(9))
print(prime_f(17))
print(prime_f(28))


# 36. Determine the prime factors of a given positive integer and their multiplicity
def prime_f_m(num):
    mult_list=[]
    final_list=[]
    factor_list=prime_f(num)
    for i in factor_list:
            multi=factor_list.count(i)
            mult_list.append(i)
            mult_list.append(multi)
            final_list.append(mult_list)
            mult_list=[]
    for i in final_list:
        once=final_list.count(i)
        if once>1:
            for j in range(once-1):
                final_list.remove(i)
    final_list=list(reversed(final_list))
    return final_list

print(prime_f_m(9))
print(prime_f_m(28))
# 37. Improved Euler's totient function

# 38. Compare the two methods of calculating Euler's totient function

# 39. A list of prime numbers in a given range

def prime_range(start, end):
    prime_list=[]
    for i in range(start, end+1):
        if is_prime(i)=='This number is prime':
            prime_list.append(i)
        

    return prime_list

print(prime_range(1, 17))

# 40. Goldbach's Conjecture
def goldbach(num):
    conjecture=[]
    finalcon=[]
    primes=prime_range(2, num)
    for i in primes:
        for j in primes:
            if i+j==num:
                conjecture.append(i)
                conjecture.append(j)
                already=list(reversed(conjecture))
                if already not in finalcon:
                    finalcon.append(conjecture)
                conjecture=[]
    return finalcon

print(goldbach(28))

# 41. A list of Goldbach Compositions
def goldbach_list(start, end):
    con=[]
    for i in range(start, end):
        if i%2==0:
            con.append(goldbach(i))
        
    for i in con:
       print(i[0][0]+i[0][1], "= ", i[0][0], "+", i[0][1])
    
goldbach_list(9, 20)


    


