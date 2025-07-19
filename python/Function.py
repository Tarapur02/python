
post=input("enter the post:")

if "Viresh".lower() in post.lower():
    print("the post talking about viresh ")
else:
    print("the post not talking about viresh ")


set=["viresh","guru","satish","sudeep","pratika"]
name=input("enter the name: ")

if name in set:
    print(f"the name {name} is present in list")
else:
    print(f"the name {name} is not present in list")



name=input("enter the name:")
if(len(name)>=10):
    print("please enter the less then 10 words ")
else:
    print("all is well !")




p1="make a lot money"
p2="boy now"
p3="you win the money"
p4="click this"
massage=input("enter the massage hera:")

if massage in(p1,p2,p3,p4):
    print("the massage is spam")
else:
    print("the massage is not a spam")





a = int(input("enter the marks of sub1: "))
b = int(input("enter the marks of sub2: "))
c = int(input("enter the marks of sub4: "))

total_percentage = 100*(a+b+c)/300

if total_percentage>=40 and a>30 and b>30 and c>30:
    print("you are passed")
else:
    print("you are failed")
if a>30:
    print("you passed in sub1")
else:
    print("you failed in sub1")
if b>30:
    print("you passed in sub2")
else:
    print("you failed in sub2")
if c>30:
    print("you passed in sub3")
else:
    print("you failed in sub3")



a = int(input("enter the  number: "))
b = int(input("enter the  number: "))
c = int(input("enter the  number: "))
d = int(input("enter the  number: "))

if a>b and a>c and a>b:
    print(" the a is the greataest  number")

elif b>a and b>c and b>d:
    print(" the b is the greataest  number")
elif c>a and c>b and c>d:
    print(" the c is the greataest  number")
else:
    print(" the d is the greataest  number")





