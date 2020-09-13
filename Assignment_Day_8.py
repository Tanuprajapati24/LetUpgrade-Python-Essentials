# Assignment Day 8 

# Question 1
#Write a decorator function for your taking input for you any kind of function you want to build,
#For example - You make a fibonacci series function,in which your input range is been defined by
#the decorator program input.

arr = []
def getInput(calculate_arg_fun):
    def wrap_function():
        print("Hey people enter two numbers =")
        a = int(input("Enter your upper limit - "))
        b = int(input("Enter your lower limit - "))
        for i in range(a,b):
            calculate_arg_fun(i)   
    return wrap_function


@getInput
def prime(num):
    check = 0
    for y in range(2,num):
        if num%y == 0 :
            check+=1
    if check==0 and num != 1:
        arr.append(num)

prime()

print(arr)
#%%

# Question 2
# For this challenge you need to develop a Python program to open a file in read only mode and try
# writing something to it and handle the subsequent errors using Exception Handling.

%%writefile test.txt

This is the test file for the exception handling in python for the python Essentials in letsupgrade B-7.

#%% 

f = open("test.txt",'r')
f.read()

#%%

try:
    f.write("my first file\n")
except:
    print("unable to write to file due to the read mode of file")
finally:
    f.close()


#%%
