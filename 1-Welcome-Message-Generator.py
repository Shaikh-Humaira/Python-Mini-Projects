# 1. Welcome Message Generator: Variables and data types
'''Description: Takes user input (name, hobby, age, color) and prints a personalized welcome message.'''
"""Concepts Used: Variables, Data Types, f-strings, Input/Output"""
#user details
name = input("What's your name? ")
hobby = input("What's your favorite hobby? ")
age = int(input("How old are you? "))
color = input("What is your favorite color? ")

#personalized welcome message
print("\n--- Welcome Message ---")
print(f"Hello, {name}! 👋")
print(f"Welcome to the world of Python Programming.")
print(f"It's great to know that you love {hobby}.")
print(f"Get ready to build something amazing today.")
print(f"You are {age} years old and {color} is a beautiful color!")
print("You're now ready to start your Python adventure 🚀🐍")

