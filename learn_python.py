#Functions!

#def say_hi(name, age):
    #print("Welc, ome Back, " + name + "!" + " You are " + age + ".")
#print("Whoah!")    
#say_hi("James", "40")    
#print("What would you like to code?")

#Return Statement!

#def cube(num):
    #return num*num*num
#result = cube(4)    
#print(result)  

#IF Statements and comparisons!

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3
        
#print(max_num(3, 40, 5))

#Building a better calculator!

num1 = float(input("Please enter your first number: "))
op = input("Enter the operator: ")
num2 = float(input("Please enter your second number: "))

if op == "+":
    print("Here is your answer: " + str(num1 + num2))
elif op == "-":
    print("Here is your answer: " + str(num1 + num2))
elif op == "/":
    print("Here is your answer: " + str(num1 + num2))
elif op == "*":
    print("Here is your answer: " + str(num1 + num2))
else:
    print("Invalid Operator!")
