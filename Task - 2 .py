#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[2]:


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

# Main program
print("Welcome to Amit's Calculator Program")

while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Check if number is even or odd")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Exiting the program...")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", divide(num1, num2))
    elif choice == "4":
        print("Result:", multiply(num1, num2))
    elif choice == "5":
        print(num1, "is even:", is_even(num1))
        print(num2, "is even:", is_even(num2))
        print(num1, "is odd:", is_odd(num1))
        print(num2, "is odd:", is_odd(num2))


# # Question2

# In[3]:


my_list = [1, 2, 3, 4, 2, 3, 1, 5, 6, 4, 7]
print("Original List:", my_list)

unique_list = list(set(my_list))

print("List without duplicates:", unique_list)


# # Question 3

# In[6]:


my_list = [9, 3, 6, 1, 10, 4, 8, 2]
print("List:", my_list)

smallest_num = min(my_list)
largest_num = max(my_list)

print("Smallest number:", smallest_num)
print("Largest number:", largest_num)


# # Question 4

# In[7]:


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print("The area of the rectangle is:", area)


# # Question 5

# In[8]:


celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = celsius * (9/5) + 32

print("The temperature in Fahrenheit is:", fahrenheit)


# # Question 6

# In[9]:


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maximum = max(num1, num2, num3)

print("The maximum number is:", maximum)


# In[ ]:




