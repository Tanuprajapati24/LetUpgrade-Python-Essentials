#%%

# Questions 1
# List and its default functions

list = ["Earth", "Sky", "Tree", "Animals"]

list1 = ["Shreya","Dhruv","Arathva","Jahanvi",[1,2,3,4,"M S doni"]]

print(list,list1)

#%%

## append method

list.append("Human")

print(list)

#%%

## insert method

list1.insert(3,"SSR")

print(list1)

#%%

## remove method

list.remove("Human")

print(list)

#%%

## indexing method

list = ["Earth", "Sky", "Tree", "Animals"]

print(list.index("Tree"))

print(list.index("Animals"))

#%%

# reverse method 

List1 = [10,2,3,13,0]

List1.sort(reverse= True)
    
print(List1)

#%%





#%%

# Questions 2
# Dictionary and its default functions.


subjectName = ['physics','chemistry','maths']
subjectMarks = [50,61,79]

print(subjectName[2])

print(subjectMarks[2])

#%%


## Return the values from dictinories.

dict1 = { 
 'physics':50,
 'chemistry':61,
 'maths':79
 }

x=dict1.values()

print(x)


#%%

## Return the keys from dictinories.:

dict1 = { 
 'physics':50,
 'chemistry':61,
 'maths':79
 }

x=dict1.keys()

print(x)

#%%

## For Insert an item to the dictionary.


dict1 = { 
 'physics':50,
 'chemistry':61,
 'maths':79
 }

dict1.update({"Hindi":84})

print(dict1)

#%%





#%%


# Questions 3
# Sets and its default functions.

fruits = {"Apple", "Banana", "Cherry"}

print(fruits)


#%%

## Adds an element to the set

fruits = {"Apple", "Banana", "Cherry"}

fruits.add("Orange")

print(fruits)

#%%

## Removes the specified element

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
#%%

## Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#%%
# Questions 4
# Tuple and explore default methods.


week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(week_days)

#%%

## Accessing the Values in a Tuple

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(weekdays[2])

#%%

## Update a Tuple.

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

weekend_days = ("Saturday", "Sunday")

print(week_days)

print(weekend_days)

#%%

## Concatenate Tuples .

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

weekend_days = ("Saturday", "Sunday")

whole_week = weekdays + weekenddays

print(week_days)

print(weekend_days)

print(whole_week)

#%%

## Delete a Tuple.

T = (1,2,3,4,5)

del T

#%%

# Questions 5
# Strings and explore default methods.

str = 'Hello Everyone'
print(str)

#%%

## Upper case the first letter in this sentence

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


#%%

##  Return the number of times the value " Song" appears in the string


txt = "I love song, songs are my favorite timepass_way"

x = txt.count("song")

print(x)

#%%

## Where in the text is the word "welcome":
    
txt = "Hello, welcome to my world"

x = txt.index("welcome")

print(x)

#%%


##  Split a string into a list where each word is a list item

txt = "welcome to the India"

x = txt.split()
print(x)


#%%
















































