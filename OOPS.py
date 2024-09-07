#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1: Bank Account Create a class representing a bank account with attributes like account number, 
# account holder name, and balance. Implement methods to deposit and withdraw money from the account.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


# In[2]:


# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID, name, 
# and salary. Implement methods to calculate the yearly bonus and display employee details.

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def yearly_bonus(self):
        bonus = self.salary * 0.10  # 10% bonus
        return bonus

    def display_details(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")


# In[3]:


# Problem 3: Vehicle Rental Create a class representing a vehicle rental system. Implement methods to rent a 
# vehicle, return a vehicle, and display available vehicles.

class VehicleRental:
    def __init__(self):
        self.available_vehicles = ["Car", "Bike", "Scooter"]

    def rent_vehicle(self, vehicle):
        if vehicle in self.available_vehicles:
            self.available_vehicles.remove(vehicle)
            print(f"{vehicle} rented!")
        else:
            print(f"{vehicle} is not available.")

    def return_vehicle(self, vehicle):
        self.available_vehicles.append(vehicle)
        print(f"{vehicle} returned!")

    def display_available_vehicles(self):
        print("Available vehicles:", self.available_vehicles)


# In[4]:


# Problem 4: Library Catalog Create classes representing a library and a book. Implement methods to add books 
# to the library, borrow books, and display available books.

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.available_books = []

    def add_book(self, book):
        self.available_books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, title):
        for book in self.available_books:
            if book.title == title:
                self.available_books.remove(book)
                print(f"Book '{title}' borrowed.")
                return
        print(f"Book '{title}' is not available.")

    def display_books(self):
        print("Available books:")
        for book in self.available_books:
            print(book.title)


# In[5]:


# Problem 5: Product Inventory Create classes representing a product and an inventory system. Implement methods to 
# add products to the inventory, update product quantity, and display available products.

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added with quantity {product.quantity}.")

    def update_quantity(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity = quantity
                print(f"Updated '{name}' to quantity {quantity}.")
                return
        print(f"Product '{name}' not found.")

    def display_products(self):
        print("Available products:")
        for product in self.products:
            print(f"{product.name}: {product.quantity}")


# In[6]:


# Problem 6: Shape Calculation Create a class representing a shape with attributes like length, width, and height. Implement methods to calculate the area and perimeter of the shape.

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# In[7]:


# Problem 7: Student Management Create a class representing a student with attributes like student ID, name, and grades. Implement methods to calculate the average grade and display student details.

class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_details(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Average Grade: {self.average_grade()}")


# In[8]:


# Problem 8: Email Management Create a class representing an email with attributes like sender, recipient, and subject. Implement methods to send an email and display email details.

class Email:
    def __init__(self, sender, recipient, subject):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject

    def send(self):
        print(f"Email sent to {self.recipient} with subject '{self.subject}'.")

    def display_details(self):
        print(f"From: {self.sender}, To: {self.recipient}, Subject: {self.subject}")


# In[9]:


# Problem 9: Social Media Profile Create a class representing a social media profile with attributes like username
#  and posts. Implement methods to add posts, display posts, and search for posts by keyword.

class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post added: {post}")

    def display_posts(self):
        print(f"Posts by {self.username}:")
        for post in self.posts:
            print(post)

    def search_posts(self, keyword):
        matching_posts = [post for post in self.posts if keyword in post]
        print(f"Posts containing '{keyword}':", matching_posts)


# In[10]:


# Problem 10: ToDo List Create a class representing a ToDo list with attributes like tasks and due dates. Implement
# methods to add tasks, mark tasks as completed, and display pending tasks.

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, due_date):
        self.tasks[task] = {'due_date': due_date, 'completed': False}
        print(f"Task '{task}' added with due date {due_date}.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task]['completed'] = True
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found.")

    def display_pending_tasks(self):
        print("Pending tasks:")
        for task, details in self.tasks.items():
            if not details['completed']:
                print(f"{task} (Due: {details['due_date']})")


# In[ ]:




