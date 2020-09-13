# Assignment Day 5 

# Question 1

#Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print
#“it’s a Match” if no then print “it’s Gone” in function


# compare the two strings 

lst1 = [1,5,6,4,1,2,3,5]
lst2 = [1,5,6,5,1,2,3,6]

lst = [1,1,5]
count = 0
r=0
for x in lst:
    for y in lst1[r:]:
        r+=1
        if (x==y):
            count+=1
            break;
        else:
            pass
        
if(count==3):
    print("it’s a Match")
else:
    print("it’s Gone")

#%%

# Question 2

# Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500

""" 
lst=list(range(1,2500))

print(lst)

lst_prime = []


lst_prime_new = filter(prime,lst)

print(list(lst_prime_num))

print()

"""  

check = 0
def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                return num
number = filter(prime,range(1,2500))

#%%

#Question 3

# Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions
# [“hey this is sai”,I am in mumbai”,....]
# o/p- [“Hey This Is Sai”, I Am In Mumbai”,....]


"""

lst=["hey this is sai”,I am in mumbai”,...."]
print(lst)

lst_new=map(lambda x: x.title(),lst)

print(list(lst_new))

"""

arr = []
st = ["hey this is sai","I am in mumbai","...."]
for x in st:
    arr.append(x.upper())
    
print(arr)

#%%















