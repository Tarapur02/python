# Print numbers from 1 to 10 using a for loop.

# Print even numbers between 1 and 50.

# Use a while loop to print numbers in reverse from 10 to 1.

# Find the sum of first 10 natural numbers.

# Print the multiplication table of a given number.

# Count the number of vowels in a string.

# Take 5 numbers from the user and print the average.

# Find the factorial of a number.

# Use a loop to print all elements in a list.

# Use a nested loop to print a right-angled triangle pattern of stars (*).

x =("viresh","sudeepa","apple","pratik")
for x in("viresh"):
    print(x)


n = int(input("enter the a number :"))

for i in range(2, n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("the number is prime")






for name in l:
    if(name.startswith("v")):
        print(f"hello {name}")


n = int(input("enter the number : "))
for i in range(1,11):
    print(f"{i*n}") 



i =1
for i in range(10):
    if(i==3):
        break
    print(i)


i=1
for i in range(7):
    if(i==6):
        continue
    print(i)




n = int(input("enter the a number :"))

for i in range(2, n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("the number is prime")




l = ["viresh","vigenesh","rahul","hero"]



name = [2,4,6,7,7,8,9,9,"guru","viresh", "hello", "sudeep"]
i = 0

while i < len(name):
    if name[i] == "viresh":
        break
    print(name[i])
    i += 1



viresh = [1, "viresh", "giresh", "harish", "hello"]
i = 0
while i < len(viresh):
    print(viresh[i])
    i += 1



i = 1
v =int(input("enter the size of your name ")) 
while (i<=v):
    x=input("enter the name letters:")
    print(x)
    i +=1
    break


i=0
while(i<5):
    print("viresh")
    i +=1


i = 0
v =int(input("enter the size of your name ")) 
while (i<=v):
    print(input("enter the name letters:"))
    i +=1






