#!/usr/bin/env python
# coding: utf-8

# # Process
# -an executable instance of a computer program
# 

# # Thread
# -is a sequence of instructions in aprogram that can be executed independently of the remaining program.

# In[2]:


from threading import*
def show():
    print("This is a child thread")
t=Thread(target=show())
t.start()
print("This is a parent thread")


# In[3]:


from threading import*
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("This is a child class")
t = MyThread()
t.start()

for i in range(5):
    print("\nThis is the main thread")
    


# # Multithreading 
# -a model where multiple threads withing a process execute independently while sharing the same resources

# In[ ]:


from threading import*
import time
class Demo:
    def num(self):
        for i in range(1,6):
            print("The number is ", i)
            time.sleep(1)
            
    def double(self):
        for i in range(1,6):
            print("The double of the number is ", 2*i)
             time.sleep(1)
                
    def square(self):
        for i in range(1,6):
            print("the square of the number is ", i * i)
             time.sleep(1)
            
obj = Demo()
t1 = Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()



# # Scripting
# - to use scriptin you import os

# In[4]:


import os

def current_directory():
    cwd=os.getcwd()
    print(cwd) #path of the current working directory

def file_path(filename):
    path= os.path.abspath(filename) #gives absolute path
    print(path)
    
current_directory()
filename = "sample.txt"
file_path(filename)


# In[7]:


import time


epc=time.time() #epic time
print(epc)
localtime=time.localtime(epc) #format to local time
print(localtime)
print(localtime.tm_year)

print(time.ctime(epc))


# In[8]:


#protocol for sending emails
import smtplib

smtpobj=smtplib.SMTP('smtp.gmail.com',587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login()


# In[10]:


from os import path

def createFile(dest):
    if not (path.isFile(dest)):
    f=open(dest,'w')
    f.write("Welcome to Python scripting")
    f.close()
    
dest = "C:\Users\lawre\sample.txt"
createFile(dest)

print("File created")


# In[ ]:




