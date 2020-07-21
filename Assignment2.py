#!/usr/bin/env python
# coding: utf-8

# In[5]:


#BackSlach
print("HelloPython!!")


# In[10]:


#Truple Quotes
print("""
 __         __
/  \.-''''-./  \
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`""")


# In[12]:


#Single Quote Inside Double Quote
print("Python's World!!")

#Or

print('Python\'s World!!')


# In[13]:


#Escape Sequences
#1.\n
print("Python\n World")
#2.\t
print("Hello \t Anybody There?")
#3.\a
print("Hello World\a")


# In[14]:


#Multiple Print Statement

name="Martha"
marks=85
age=18

print("Method 1:\n")
print("The name of student is :",name,"marks obtained are :",marks,"and age is :",age)

print("Method 2:\n")

print("The name of student is : %s marks obtained are : %f and age is : %d"%(name,marks,age))


# In[15]:


#Accuracy In Float
marks=58.98567
print("The Marks obtained are : %10.2f "%(marks))


# In[16]:


#Assignment Operator

x=20
y=x
print(y)


# In[48]:


#Operators:

print("1.Arithmetic Operator\n")
a=40
b=10
c=2
d=3
print(a,"+",b,"=",a+b)
print(a,"*",b,"=",a*b)
print(a,"-",b,"=",a-b)
print(a,"/",b,"=",a/b)
print(a,"%",b,"=",a%b)
print(c,"**",d,"=",c**d)

print("\n2.Comparision Operator\n")

print(a,"=",b,"=",a==b)
print(a,">",b,"=",a>b)
print(a,"<",b,"=",a<b)
print(a,">=",b,"=",a>=b)
print(a,"<=",b,"=",a<=b)

print("\n3.Assignment Operator\n")

a+=1
print("a+=1 => ",a)

a-=1
print("a-=1 => ",a)

a/=1
print("a/=1 =>",a)

c**=d
print("c**=d =>",c)

print("\n4.Bitwise Operator\n")

bit1=10
bit2=24

print(bit1,"|",bit2,"=",bit1|bit2)
print(bit1,"&",bit2,"=",bit1&bit2)
print("~",bit1,"=",~bit1)

print("\n5.Logical Operator\n")

print("10>9 and 10<75 ->",10>9 and 10<75)
print("10<9 or 10>75 ->",10<9 and 10<75)


print("\n6.Membership Operator\n")

str="Programming"
print("str=Programming")
print("m in str","m" in str)
print("m in str","m" not in str)

print("\n7.Identity Operator\n")

num=10
num1=10

print(num, "is" ,num1,"->",num is num1)
print(num, "is not" ,num1,"->",num is not num1)







# In[50]:


print("10>8>9")
10>8>9


# In[51]:


2**-1

