#%%

# assignment - 2

# Question 1

# You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
# 1000ft, if it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
# the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
# later”

    
    
 
altitude = input("enter any number-")
altitude = int(altitude)
if altitude == 1000:
    print("safe to land")
elif altitude < 5000:
    print("bring down to 1000ft")
else:
    print("turn around and try later")


altitude = input("enter any number-")
altitude = int(altitude)
if altitude == 1000: 
    print("safe to land")
elif altitude < 5000: 
    print("bring down to 1000ft")
else: 
    print("turn around and try later")

altitude = input("enter any number-")
altitude = int(altitude)
if altitude == 1000:
    print("safe to land")
elif altitude < 5000: 
    print("bring down to 1000ft")
else: 
    print("turn around and try later")   
    

#%%

# Question 2
# Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
# function.



starting_point = 1
ending_point = 200+1
  
for i in range(starting_point,ending_point): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)
        
#%%