import constant

# num1 = True ; 
# num2 = "string" 
# num3 = 145 ;

num1 , num2 , num3 = True , "string" ,145  
print('old values of num 1' ,num1,'num3 : ' , num3)
num3 = num1 = 45 
# make a return from this

print('hello and welcom to this letter \n', sep='', end='')


# use same constant 

print('PI :',constant.PI,'Gravity :',constant.GRAVITY) 

# Python numeric literals 
print('Python numeric literals__________')
#Decimal 10 2
#Binary 
binary_number = 0b100 # writing in Decimal 
print('binary numbre of 100 :',binary_number)
#Octal 
octal_number  = 0o10
print('octal number of 10 :',octal_number)
#Hexadecimal 
hexadecimal_number = 0xA 
print('hexadecimal number A:',hexadecimal_number)
#Floating-point literal 10.5 11.6   
#Complex literal of form of a +bj a is real and bj is imagination part 
complex_number = (6 + 8j) + (1 +2j)  
print('complex number  (6 + 8j) + (1 +2j) :',complex_number)

# list literal
fruits = ["apple", "mango", "orange"] 
fruits[0] = 'samsung'
print(fruits)

# tuple literal
numbers = (1, 2, 3) 
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}  #like obj 

print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)