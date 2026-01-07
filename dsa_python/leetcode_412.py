from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        my_list=[]

        for i in range(1,n+1):
            if i % 3==0 and i%5==0:
                my_list.append("FuzzBuzz")
            elif i%3==0:
                my_list.append("Fuzz")
            elif i%5==0:
                my_list.append("Buzz")
            else:
                my_list.append(str(i))

        return my_list
    



n=int(input("enter the number: "))

fizz=Solution()

print(fizz.fizzBuzz(n))


                




        