'''
intuition: 
A generator expression is a concise way to create a generator without the need to define a separate function. 
It is similar to a list comprehension, but instead of creating a list, it creates a generator. 
The generator expression uses a syntax similar to list comprehensions, but it uses parentheses () instead of square brackets [].


'''
s=input()
print(any(i.isalpha() for i in s))
print(any(i.isalnum() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
