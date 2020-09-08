# Question 1
# Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon
# as you encounter the first armstrong number.
# Use while loop


lower = 1042000
upper = 702648265
for num in range(lower,upper + 1): 
    order = len(str(num)) 
    sum = 0 
    temp = num
while temp > 0: 
    digit = temp % 10 
    sum += digit ** order
    temp //= 10 
if num == sum: 
    print("The first Armstrong number is , num") 

#%%
