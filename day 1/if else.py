Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input())
b=int(input())
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'b=int(input())'
>>> a=int(input("enter the number:"))
enter the number:2
>>> b=int(input("enter the number:"))
enter the number:1
>>> if(a>b):
...     print('a is greater')
... else:
...     print('b is greater')
... 
...     
a is greater
